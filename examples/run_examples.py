#!/usr/bin/env python3
"""Run the src/ modules on real public data and save figures to docs/figures/.

Data (all public, downloaded on demand):
  scRNA     scanpy.datasets.pbmc3k (10x PBMC 3k)
  spatial   squidpy.datasets.visium_hne_adata (10x Visium mouse brain)
  scATAC    10x PBMC 3k Multiome peak matrix (--multiome-h5)
  QC        SARS-CoV-2 Illumina reads ENA ERR10730304 (--fastq)
  variants  VCF from nf-variant-pipeline example_results (--vcf)

Usage: python examples/run_examples.py [--only scrna,spatial,scatac,qc,variants]
"""
import argparse, gzip, os, sys
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np, pandas as pd
import scanpy as sc

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT / "docs" / "figures"; FIG.mkdir(parents=True, exist_ok=True)
for m in ("scrna_scanpy", "spatial_transcriptomics", "scatac_scanpy", "quality_control", "variant_analysis"):
    sys.path.insert(0, str(ROOT / "src" / m))
sc.settings.set_figure_params(dpi=100, facecolor="white")

def save(name):
    plt.savefig(FIG / f"{name}.png", dpi=120, bbox_inches="tight"); plt.close("all")

def scrna():
    import scrna_scanpy as m
    ad = sc.datasets.pbmc3k()
    ad.var["mt"] = ad.var_names.str.startswith("MT-")
    sc.pp.calculate_qc_metrics(ad, qc_vars=["mt"], inplace=True)
    sc.pl.violin(ad, ["n_genes_by_counts", "total_counts", "pct_counts_mt"], multi_panel=True, show=False)
    save("scrna_qc")
    ad = m.process_scrna_scanpy(ad)
    sc.pl.umap(ad, color="leiden", show=False, title=f"PBMC 3k: {ad.obs.leiden.nunique()} Leiden clusters")
    save("scrna_umap")
    print("scrna:", ad.n_obs, "cells")

def spatial():
    import squidpy as sq, spatial_transcriptomics as m
    ad = sq.datasets.visium_hne_adata()
    ad.uns.pop("leiden_colors", None)
    ad = m.process_spatial_data(ad)
    m.spatial_analysis(ad)
    sc.pl.spatial(ad, color="leiden", show=False); save("spatial_clusters")
    top = ad.uns["moranI"].head(6).index.tolist()
    sc.pl.spatial(ad, color=top, ncols=3, show=False); save("spatial_moran_top")
    print("spatial top Moran:", top)

def scatac(h5):
    import scatac_scanpy as m
    ad = sc.read_10x_h5(h5, gex_only=False)
    ad = ad[:, ad.var["feature_types"] == "Peaks"].copy(); ad.var_names_make_unique()
    ad = m.process_scatac_scanpy(ad)
    sc.pl.umap(ad, color="leiden", show=False, title=f"PBMC Multiome ATAC peaks: {ad.obs.leiden.nunique()} clusters")
    save("scatac_umap")
    print("scatac:", ad.n_obs, "cells")

def qc(fastq, n=50000):
    import quality_control as m
    q, gc = [], []
    with gzip.open(fastq, "rt") as fh:
        for i, line in enumerate(fh):
            if i % 4 == 1:
                s = line.strip(); gc.append((s.count("G") + s.count("C")) / max(len(s), 1))
            elif i % 4 == 3:
                q.append(np.mean([ord(c) - 33 for c in line.strip()]))
            if len(q) >= n and len(gc) >= n: break
    df = pd.DataFrame({"quality": q, "gc_content": gc})
    print("qc:", m.calculate_qc_metrics(df))
    cwd = os.getcwd(); os.chdir(FIG)
    m.plot_quality_distribution(df); os.chdir(cwd)
    (FIG / "quality_distribution.png").rename(FIG / "qc_quality_distribution.png")
    plt.figure(figsize=(6, 4)); plt.hist(df.gc_content, bins=40, color="#55a868")
    plt.xlabel("GC fraction per read"); plt.ylabel("reads"); plt.title("GC content"); save("qc_gc_content")

def variants(vcf):
    import variant_analysis as m
    df = m.load_vcf(vcf)
    df = m.annotate_variants(df)
    
    kind = np.where((df.REF.str.len() == 1) & (df.ALT.str.len() == 1), "SNV", "indel")
    ts = {"AG", "GA", "CT", "TC"}
    snv = df[kind == "SNV"]
    tstv = sum((a + b) in ts for a, b in zip(snv.REF, snv.ALT)), len(snv)
    fig, axs = plt.subplots(1, 2, figsize=(9, 3.5))
    pd.Series(kind).value_counts().plot.bar(ax=axs[0], color="#4c72b0", rot=0); axs[0].set_title("Variant types")
    axs[1].bar(df.POS.astype(str), df.QUAL, color="#c44e52"); axs[1].set_title("QUAL by position")
    axs[1].tick_params(axis="x", labelrotation=90, labelsize=6)
    fig.tight_layout(); save("variants_summary")
    print(f"variants: {len(df)} calls, transitions {tstv[0]}/{tstv[1]} SNVs")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="scrna,spatial,scatac,qc,variants")
    ap.add_argument("--multiome-h5", default="../scATAC-WNN-multimodal/data/pbmc_unsorted_3k_filtered_feature_bc_matrix.h5")
    ap.add_argument("--fastq", default="../nf-variant-pipeline/test_data/sample1_R1.fastq.gz")
    ap.add_argument("--vcf", default="../nf-variant-pipeline/example_results/sample1.filtered.vcf.gz")
    a = ap.parse_args()
    for step in a.only.split(","):
        {"scrna": scrna, "spatial": spatial, "scatac": lambda: scatac(a.multiome_h5),
         "qc": lambda: qc(a.fastq), "variants": lambda: variants(a.vcf)}[step]()
