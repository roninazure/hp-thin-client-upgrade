# Script Name: ThinPro Version Parser
# Description: This script parses a file containing entries of ThinPro systems, 
#              identifying those with a specific version (8.0.0) and printing their details.
# Usage: Call parse_file(filename) with the path to the file containing the ThinPro system entries.
# Note: The file should follow a specific format where each entry starts with 'WS' and contains 
#       key-value pairs, one per line.

def parse_file(filename):
    with open(filename, 'r') as file:
        current_entry = {}
        for line in file:
            # Check if the line indicates a new entry (hostname and IP)
            if line.startswith('WS'):
                # Check if the current entry meets the criteria
                if current_entry.get('DISTRIB_RELEASE') == '8.0.0' or \
                   current_entry.get('DISTRIB_DESCRIPTION') == '"ThinPro 8.0.0"':
                    # Print hostname (including IP) and DISTRIB_DESCRIPTION
                    print({
                        'hostname': current_entry.get('hostname', ''),
                        'DISTRIB_DESCRIPTION': current_entry.get('DISTRIB_DESCRIPTION', 'Unavailable')
                    })

                # Reset current_entry for new entry
                current_entry = {'hostname': line.strip()}

            # Process other lines as key-value pairs
            elif '=' in line:
                key, value = line.strip().split('=', 1)
                current_entry[key] = value

        # Check the last entry after finishing the file
        if current_entry.get('DISTRIB_RELEASE') == '8.0.0' or \
           current_entry.get('DISTRIB_DESCRIPTION') == '"ThinPro 8.0.0"':
            print({
                'hostname': current_entry.get('hostname', ''),
                'DISTRIB_DESCRIPTION': current_entry.get('DISTRIB_DESCRIPTION', 'Unavailable')
            })

# Replace 'thinpro_versions_temp.txt' with the path to your file
parse_file('thinpro_versions_temp.txt')

