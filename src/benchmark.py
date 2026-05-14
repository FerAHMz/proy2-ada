"""
Benchmark de DP exacta vs FFD greedy para Bin Packing.

Corre ambos algoritmos sobre las 72 instancias del generador, mide el tiempo
con time.perf_counter, calcula el ratio FFD/OPT y guarda los resultados:
  - results/tiempos.csv
  - results/scatter.png  (entregable 5b)
  - results/regresion.md (entregable 5c)
"""

import csv
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(__file__).parent))
from generator import all_instances
from dp_bitmask import bin_packing_dp
from greedy_ffd import bin_packing_ffd


RESULTS_DIR = Path(__file__).resolve().parent.parent / "results"
FFD_RUNS = 7
DP_RUNS_SMALL = 3
DP_REPEAT_LIMIT = 14


def time_call(func, items, capacity, runs):
    """Corre la funcion varias veces y devuelve el mejor tiempo y el resultado."""
    best = float("inf")
    result = None
    for _ in range(runs):
        t0 = time.perf_counter()
        result = func(list(items), capacity)
        t1 = time.perf_counter()
        if t1 - t0 < best:
            best = t1 - t0
    return best, result


def run_benchmark():
    rows = []
    instances = all_instances()
    total = len(instances)
    for i, inst in enumerate(instances, 1):
        cap = inst.capacity
        items = list(inst.items)

        ffd_t, (ffd_bins, _) = time_call(bin_packing_ffd, items, cap, FFD_RUNS)

        #para n grande la DP tarda mucho, una sola corrida basta
        dp_runs = DP_RUNS_SMALL if inst.n <= DP_REPEAT_LIMIT else 1
        dp_t, (dp_bins, _) = time_call(bin_packing_dp, items, cap, dp_runs)

        ratio = ffd_bins / dp_bins if dp_bins > 0 else 1.0
        rows.append({
            "id": inst.id,
            "n": inst.n,
            "capacity": cap,
            "distribution": inst.distribution,
            "seed": inst.seed,
            "ffd_time_s": ffd_t,
            "dp_time_s": dp_t,
            "ffd_bins": ffd_bins,
            "dp_bins": dp_bins,
            "ratio_ffd_over_opt": ratio,
        })
        print(
            f"[{i:2d}/{total}] {inst.id}: "
            f"ffd={ffd_t*1000:.3f}ms ({ffd_bins}b), "
            f"dp={dp_t:.4f}s ({dp_bins}b), "
            f"ratio={ratio:.3f}"
        )
    return rows


def save_csv(rows, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def plot_scatter(rows, path):
    ns = [r["n"] for r in rows]
    ffd_t = [r["ffd_time_s"] for r in rows]
    dp_t = [r["dp_time_s"] for r in rows]

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    axes[0].scatter(ns, ffd_t, alpha=0.7, color="tab:blue", label="FFD")
    axes[0].scatter(ns, dp_t, alpha=0.7, color="tab:red", label="DP")
    axes[0].set_xlabel("n")
    axes[0].set_ylabel("tiempo (s)")
    axes[0].set_title("Tiempo vs n (escala lineal)")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    axes[1].scatter(ns, ffd_t, alpha=0.7, color="tab:blue", label="FFD")
    axes[1].scatter(ns, dp_t, alpha=0.7, color="tab:red", label="DP")
    axes[1].set_yscale("log")
    axes[1].set_xlabel("n")
    axes[1].set_ylabel("tiempo (s, log)")
    axes[1].set_title("Tiempo vs n (escala log)")
    axes[1].legend()
    axes[1].grid(True, alpha=0.3, which="both")

    plt.suptitle("Bin Packing: tiempos de ejecucion DP vs FFD")
    plt.tight_layout()
    plt.savefig(path, dpi=120)
    plt.close()


def fit_polys(ns, ts, max_degree=5):
    """Ajusta polinomios de grado 1..max_degree y devuelve (grado, coefs, R^2)."""
    ns_arr = np.array(ns, dtype=float)
    ts_arr = np.array(ts, dtype=float)
    fits = []
    for deg in range(1, max_degree + 1):
        coeffs = np.polyfit(ns_arr, ts_arr, deg)
        pred = np.polyval(coeffs, ns_arr)
        ss_res = np.sum((ts_arr - pred) ** 2)
        ss_tot = np.sum((ts_arr - ts_arr.mean()) ** 2)
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0
        fits.append((deg, coeffs, r2))
    return fits


def write_regression_md(rows, path):
    ns = [r["n"] for r in rows]
    ffd_t = [r["ffd_time_s"] for r in rows]
    dp_t = [r["dp_time_s"] for r in rows]

    ffd_fits = fit_polys(ns, ffd_t)
    dp_fits = fit_polys(ns, dp_t)
    best_ffd = max(ffd_fits, key=lambda x: x[2])
    best_dp = max(dp_fits, key=lambda x: x[2])

    #para DP tambien ajusto log(t) = a*n + b -> t = e^b * (e^a)^n
    log_dp = np.log(np.maximum(dp_t, 1e-12))
    a, b = np.polyfit(np.array(ns, dtype=float), log_dp, 1)
    base = float(np.exp(a))
    factor = float(np.exp(b))

    avg_ratio = float(np.mean([r["ratio_ffd_over_opt"] for r in rows]))
    max_ratio = float(np.max([r["ratio_ffd_over_opt"] for r in rows]))

    lines = [
        "# Regresion polinomial (entregable 5c)",
        "",
        "Se ajustan polinomios de grado 1 a 5 sobre los tiempos medidos en",
        "`results/tiempos.csv`. Para cada grado se reporta el coeficiente de",
        "determinacion R^2 para ver cual ajusta mejor.",
        "",
        "## FFD (greedy)",
        "",
        "| grado | R^2 | coeficientes (mayor a menor) |",
        "|---|---|---|",
    ]
    for deg, coeffs, r2 in ffd_fits:
        coef_str = [float(round(c, 10)) for c in coeffs]
        lines.append(f"| {deg} | {r2:.4f} | {coef_str} |")
    lines += [
        "",
        f"**Mejor ajuste FFD: grado {best_ffd[0]}, R^2 = {best_ffd[2]:.4f}.**",
        "",
        "La teoria predice O(n log n + n^2) ≈ O(n^2) para la implementacion",
        "ingenua. El ajuste cuadratico suele dar muy buen R^2, lo que concuerda",
        "con el analisis del docs/04-complejidad.md.",
        "",
        "## DP exacta",
        "",
        "| grado | R^2 | coeficientes (mayor a menor) |",
        "|---|---|---|",
    ]
    for deg, coeffs, r2 in dp_fits:
        coef_str = [float(round(c, 10)) for c in coeffs]
        lines.append(f"| {deg} | {r2:.4f} | {coef_str} |")
    lines += [
        "",
        f"**Mejor ajuste polinomial DP: grado {best_dp[0]}, R^2 = {best_dp[2]:.4f}.**",
        "",
        "Un polinomio de grado alto puede dar R^2 razonable, pero la DP no es",
        "polinomial sino exponencial. Para verlo mejor se ajusta log(t) = a·n + b:",
        "",
        f"- pendiente a = {a:.4f}",
        f"- t ≈ {factor:.4e} · {base:.4f}^n",
        "",
        f"La base empirica ({base:.4f}) se compara con el 3 teorico del analisis",
        "asintotico O(3^n). Constantes y overhead de Python explican la",
        "diferencia entre ambos valores.",
        "",
        "## Calidad de la solucion greedy",
        "",
        f"- Ratio promedio FFD/OPT: **{avg_ratio:.4f}**",
        f"- Ratio maximo FFD/OPT: **{max_ratio:.4f}**",
        "",
        "La cota teorica conocida es FFD ≤ (11/9)·OPT + 6/9 ≈ 1.222·OPT + 0.667.",
        "Los ratios medidos quedan por debajo de esa cota, como se esperaba.",
    ]

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def main():
    print("=== Benchmark Bin Packing: DP vs FFD ===")
    rows = run_benchmark()

    csv_path = RESULTS_DIR / "tiempos.csv"
    save_csv(rows, csv_path)
    print(f"\nCSV guardado en {csv_path}")

    scatter_path = RESULTS_DIR / "scatter.png"
    plot_scatter(rows, scatter_path)
    print(f"Scatter guardado en {scatter_path}")

    reg_path = RESULTS_DIR / "regresion.md"
    write_regression_md(rows, reg_path)
    print(f"Regresion guardada en {reg_path}")


main()
