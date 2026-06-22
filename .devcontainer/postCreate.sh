#!/usr/bin/env bash
set -e

mkdir -p notebooks pcap_files csv_raw

echo "=== Python ==="
python --version

echo "=== scapy ==="
python -c "import scapy; print(scapy.__version__)"

echo "=== cicflowmeter ==="
python -c "import importlib.metadata as md; print(md.version('cicflowmeter'))"

echo "=== listo ==="
