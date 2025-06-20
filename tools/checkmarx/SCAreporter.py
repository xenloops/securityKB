# First create a file scan_ids.txt, containing one scan ID per line.
# Run like:
# python3 SCAreporter.py

import subprocess
import json
import csv

# Define a function to extract SCA data from Checkmarx CLI for a given scan ID
def get_sca_data(scan_id):
    # Run the Checkmarx CLI command to fetch SCA data for the scan
    try:
        command = ["cx", "sca", "results", "get", "--scan-id", scan_id, "--output-format", "json"]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        scan_data = json.loads(result.stdout)
        
        # Extract the necessary fields from the scan data
        dependencies = []
        for dependency in scan_data.get("dependencies", []):
            repo_name = dependency.get("repository", "N/A")
            package_name = dependency.get("name", "N/A")
            package_version = dependency.get("version", "N/A")
            package_license = dependency.get("license", "N/A")
            cves = ', '.join(dependency.get("cves", [])) if "cves" in dependency else "N/A"
            purl = dependency.get("purl", "N/A")
            
            # Collect data for each dependency
            dependencies.append([repo_name, package_name, package_version, package_license, cves, purl])
        
        return dependencies
    except subprocess.CalledProcessError as e:
        print(f"Error fetching data for scan ID {scan_id}: {e.stderr.decode()}")
        return []

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

# Main function to orchestrate the scanning and CSV writing
def main(scan_ids_file, output_csv_file):
    # Read scan IDs from the provided file
    scan_ids = read_scan_ids(scan_ids_file)
    if not scan_ids:
        return
    
    all_dependencies = []
    
    # For each scan ID, extract the SCA data and store the results
    for scan_id in scan_ids:
        print(f"Processing scan ID: {scan_id}")
        dependencies = get_sca_data(scan_id)
        all_dependencies.extend(dependencies)
    
    # Write the collected data to a CSV file
    write_to_csv(all_dependencies, output_csv_file)

# If this script is being run directly, start the process
if __name__ == "__main__":
    # Specify the input file with scan IDs and the output CSV file
    scan_ids_file = "scan_ids.txt"  # Input file with scan IDs (one per line)
    output_csv_file = "sca_dependencies.csv"  # Output CSV file
    
    main(scan_ids_file, output_csv_file)
