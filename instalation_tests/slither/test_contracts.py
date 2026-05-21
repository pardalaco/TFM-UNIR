#!/usr/bin/env python3
import argparse
import subprocess
import os
import re
from collections import Counter

def get_solidity_version(contract_path):
    """Extract Solidity version from pragma statement."""
    try:
        with open(contract_path, 'r') as f:
            for line in f:
                match = re.search(r'pragma\s+solidity\s+([^;]+)', line)
                if match:
                    version_str = match.group(1).strip()
                    version_match = re.search(r'(\d+\.\d+\.\d+)', version_str)
                    if version_match:
                        return version_match.group(1)
    except:
        pass
    return "Unknown"

def find_sol_files(directory):
    """Find all .sol files in directory and subdirectories."""
    sol_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.sol'):
                sol_files.append(os.path.join(root, file))
    return sorted(sol_files)

def test_contract(contract_path):
    """Test a single contract and return results."""
    contract_name = os.path.basename(contract_path)
    solidity_version = get_solidity_version(contract_path)

    try:
        result = subprocess.run(
            ["python", "analyze_contract.py", contract_path],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode == 0:
            execution = "Success"
            output = result.stdout.strip()
        else:
            execution = "Failed"
            output = result.stderr.strip()[:200]
    except subprocess.TimeoutExpired:
        execution = "Timeout"
        output = ""
    except Exception as e:
        execution = f"Error: {str(e)}"
        output = ""

    return {
        "contract": contract_name,
        "path": contract_path,
        "version": solidity_version,
        "execution": execution,
        "output": output
    }

def main():
    parser = argparse.ArgumentParser(description="Test all contracts in subfolders")
    parser.add_argument("directory", help="Directory to scan for .sol files")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: {args.directory} is not a valid directory")
        return

    sol_files = find_sol_files(args.directory)

    if not sol_files:
        print(f"No .sol files found in {args.directory}")
        return

    print(f"Found {len(sol_files)} contract(s)")
    print("=" * 80)

    # Inicializar contador
    stats = Counter()

    for sol_file in sol_files:
        result = test_contract(sol_file)

        # Actualizar contador
        stats[result['execution']] += 1

        print(f"\nContract: {result['contract']}")
        print(f"Path: {result['path']}")
        print(f"Solidity Version: {result['version']}")
        print(f"Execution: {result['execution']}")
        if result['output']:
            print(f"Output:\n{result['output']}")
        print("-" * 80)

    # Resumen final
    print("\n" + "=" * 30)
    print("       TEST SUMMARY")
    print("=" * 30)
    print(f"Total contracts:  {len(sol_files)}")
    for status, count in stats.items():
        print(f"{status:15}:  {count}")
    print("=" * 30)

if __name__ == "__main__":
    main()
