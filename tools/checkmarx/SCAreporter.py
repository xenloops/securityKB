# First create a file scan_ids.txt, containing one scan ID per line.
# Run like:
# python3 SCAreporter.py

#!/usr/bin/env python3
import csv
import json
import subprocess
import sys
import os

exec_cx = "path/to/checkmarx/cli/tool"

# File settings
SCAN_ID_FILE = 'scan_ids.txt'
OUTPUT_CSV_FILE = 'sca_results.csv'
TEMP_JSON_FILE = 'sca_temp_output.json'


# Define a function to extract SCA data from Checkmarx CLI for a given scan ID
def run_cx_scan(scan_id, json_output_file):
    """
    Runs the Checkmarx CLI to get SCA scan results and outputs to a file.
    """
    try:
        cmd = [
            exec_cx, "results", "show", 
            "--sca-hide-dev-test-dependencies", 
            "--scan-id", scan_id, 
            "--report-format", "json", 
            "--report-sbom-format", "CycloneDX", 
            "--output-name", json_output_file
        ]
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running Checkmarx CLI for scan ID {scan_id}: {e}", file=sys.stderr)
        return False

# Define a function to read scan IDs from a text file
def read_scan_ids(filename):
    try:
        with open(filename, 'r') as f:
            scan_ids = [line.strip() for line in f.readlines()]
        return scan_ids
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return []

# Define a function to write data to a CSV file
def write_to_csv(data, output_file):
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write the header row
            csv_writer.writerow(["Repository", "Package Name", "Package Version", "Package License", "CVEs Found", "Package URL (PURL)"])
            # Write the data rows
            csv_writer.writerows(data)
        print(f"Data has been written to {output_file}.")
    except Exception as e:
        print(f"Error writing to CSV file: {e}")

def load_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to load JSON file {filepath}: {e}", file=sys.stderr)
        return None

def process_scan_data(scan_data):
    rows = []

    repository = scan_data.get('repository', '') or scan_data.get('project', {}).get('name', '')

    # Find the first SCA result section
    sca_result = None
    for result in scan_data.get('results', []):
        if result.get('type') == 'sca':
            sca_result = result
            break

    if not sca_result:
        print("⚠️ No SCA results found in scan data.", file=sys.stderr)
        return rows

    dependencies = sca_result.get('dependencies', [])
    if not dependencies:
        print("⚠️ No dependencies found in SCA result.", file=sys.stderr)

    for dependency in dependencies:
        pkg_name = dependency.get('packageName', '')
        pkg_version = dependency.get('version', '')
        pkg_license = dependency.get('license', '')
        cves = dependency.get('cves', [])
        cves_str = "; ".join(cves) if isinstance(cves, list) else str(cves)
        purl = dependency.get('purl', '')

        row = {
            'Repository': repository,
            'Package Name': pkg_name,
            'Package Version': pkg_version,
            'Package License': pkg_license,
            'CVEs': cves_str,
            'PURL': purl
        }
        rows.append(row)

    return rows

# def process_scan_data(scan_data):
#     """
#     Extracts the required data from the scan JSON.
#     """
#     rows = []
#     repository = scan_data.get('repository', '')

#     dependencies = scan_data.get('dependencies', [])
#     for dependency in dependencies:
#         pkg_name = dependency.get('packageName', '')
#         pkg_version = dependency.get('version', '')
#         pkg_license = dependency.get('license', '')
#         cves = dependency.get('cves', [])
#         cves_str = "; ".join(cves) if isinstance(cves, list) else str(cves)
#         purl = dependency.get('purl', '')

#         row = {
#             'Repository': repository,
#             'Package Name': pkg_name,
#             'Package Version': pkg_version,
#             'Package License': pkg_license,
#             'CVEs': cves_str,
#             'PURL': purl
#         }
#         rows.append(row)
#     return rows

# Main function to orchestrate the scanning and CSV writing
def main():
    all_rows = []

    # Read scan IDs
    try:
        with open(SCAN_ID_FILE, 'r', encoding='utf-8') as f:
            scan_ids = [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Failed to read scan IDs: {e}", file=sys.stderr)
        sys.exit(1)

    if not scan_ids:
        print("No scan IDs found.", file=sys.stderr)
        sys.exit(1)

    for scan_id in scan_ids:
        print(f"Processing scan ID: {scan_id}")
        
        if run_cx_scan(scan_id, TEMP_JSON_FILE):
            scan_data = load_json_file(TEMP_JSON_FILE)
            if scan_data:
                rows = process_scan_data(scan_data)
                all_rows.extend(rows)
            else:
                print(f"Failed to parse scan data for scan ID {scan_id}", file=sys.stderr)
        else:
            print(f"Scan command failed for scan ID {scan_id}", file=sys.stderr)

        # Clean up temp file if it exists
        if os.path.exists(TEMP_JSON_FILE):
            os.remove(TEMP_JSON_FILE)

    if not all_rows:
        print("No data collected from scans.", file=sys.stderr)
        sys.exit(1)

    # Write to CSV
    fieldnames = ['Repository', 'Package Name', 'Package Version', 'Package License', 'CVEs', 'PURL']
    try:
        with open(OUTPUT_CSV_FILE, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_rows)
        print(f"CSV written to {OUTPUT_CSV_FILE}")
    except Exception as e:
        print(f"Failed to write CSV: {e}", file=sys.stderr)
        sys.exit(1)

# If this script is being run directly, start the process
if __name__ == "__main__":
    main()
