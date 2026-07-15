#!/usr/bin/env bash
# Download GSE120575 supplementary files from GEO.
# Sade-Feldman et al., Cell 2018 — melanoma ICB scRNA-seq (Smart-seq2, CD45+ TILs).
# Not tracked in git: the TPM matrix is ~121 MB, over GitHub's 100 MB per-file limit.
# Usage: bash scripts/download_data.sh

set -euo pipefail

DATA_DIR="data"
BASE="https://ftp.ncbi.nlm.nih.gov/geo/series/GSE120nnn/GSE120575/suppl"
TPM="GSE120575_Sade_Feldman_melanoma_single_cells_TPM_GEO.txt.gz"
META="GSE120575_patient_ID_single_cells.txt.gz"

mkdir -p "${DATA_DIR}"

fetch () {
  local file="$1"
  if [[ -f "${DATA_DIR}/${file}" ]]; then
    echo "[skip] ${file} already present"
  else
    echo "[get ] ${file}"
    curl -L --fail --progress-bar -o "${DATA_DIR}/${file}" "${BASE}/${file}"
  fi
}

fetch "${TPM}"
fetch "${META}"

echo; echo "Downloaded to ${DATA_DIR}/:"; ls -lh "${DATA_DIR}"
echo; echo "Sanity check — expect 16292 columns (1 gene column + 16291 cells):"
gzip -dc "${DATA_DIR}/${TPM}" | head -1 | awk -F'\t' '{print NF}'
echo; echo "Metadata header should be on line 20:"
gzip -dc "${DATA_DIR}/${META}" | grep -n "Sample name" | head -1 | cut -c1-60
