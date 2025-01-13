import json
import glob

def combine_json_files(input_files, output_file):
    combined_data = []

    # Iterate through all input files
    for file_name in input_files:
        with open(file_name, 'r') as f:
            data = json.load(f)
            combined_data.extend(data)  # Add the content of each file to the combined list

    # Write the combined data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(combined_data, f, indent=4)

# Example usage
input_files = ['hostel_a.json', 'hostel_b.json', 'hostel_c.json', 'hostel_d.json', 'hostel_e.json']
output_file = 'combined_hostels.json'
combine_json_files(input_files, output_file)

print(f"Combined JSON saved to {output_file}.")
