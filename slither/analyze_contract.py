#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
import re

def get_solidity_version(contract_path):
    """Extract Solidity version from pragma statement."""
    with open(contract_path, 'r') as f:
        for line in f:
            match = re.search(r'pragma\s+solidity\s+([^;]+)', line)
            if match:
                version_str = match.group(1).strip()
                # Extract first version number (handle ^0.4.15, >=0.4.15, etc.)
                version_match = re.search(r'(\d+\.\d+\.\d+)', version_str)
                if version_match:
                    return version_match.group(1)
    return None

def setup_solc_version(version):
    """Install and select the required Solidity version."""
    print(f"Setting up Solidity version {version}...")
    try:
        subprocess.run(["solc-select", "install", version], capture_output=True)
        subprocess.run(["solc-select", "use", version], check=True, capture_output=True)
        print(f"Using Solidity {version}")
    except subprocess.CalledProcessError as e:
        print(f"Warning: Could not set solc version: {e}")
    except FileNotFoundError:
        print("Warning: solc-select not found. Install with: pip install solc-select")

def main():
    parser = argparse.ArgumentParser(description="Analyze smart contract with Slither and count vulnerabilities by severity.")
    parser.add_argument("contract", help="Path to the Solidity contract file")
    args = parser.parse_args()

    # Auto-detect and setup Solidity version
    version = get_solidity_version(args.contract)
    if version:
        setup_solc_version(version)
    else:
        print("Warning: Could not detect Solidity version from pragma")

    cmd = ["slither", args.contract, "--json", "-"]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
    except FileNotFoundError:
        print("Error: slither not found. Make sure it is installed and in PATH.")
        sys.exit(1)

    # Slither may return non-zero on findings, but still output JSON
    if result.returncode != 0 and not result.stdout:
        print(f"Slither failed:\n{result.stderr}")
        sys.exit(1)

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("Failed to parse Slither JSON output.")
        print("Stdout:", result.stdout[:500])
        print("Stderr:", result.stderr[:500])
        sys.exit(1)

    # Count by impact
    counts = {}
    # Slither JSON structure: data might have "detectors" or "results"
    # According to slither docs, the JSON output contains a list of detectors under "detectors"
    detectors = data.get("results", {}).get("detectors", [])
    for detector in detectors:
        impact = detector.get("impact", "Unknown")
        counts[impact] = counts.get(impact, 0) + 1

    # Print sorted by severity order
    severity_order = ["Critical", "High", "Medium", "Low", "Informational", "Optimization", "Unknown"]
    for sev in severity_order:
        if sev in counts:
            print(f"{sev}: {counts[sev]}")
    # Print any other severities not in order
    for sev, cnt in sorted(counts.items()):
        if sev not in severity_order:
            print(f"{sev}: {cnt}")

if __name__ == "__main__":
    main()
