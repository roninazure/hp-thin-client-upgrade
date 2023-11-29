def parse_file(filename):
    with open(filename, 'r') as file:
        current_entry = {}
        for line in file:
            # Check if the line indicates a new entry
            if line.startswith('WS'):
                # Check if the current entry meets the criteria
                if current_entry.get('DISTRIB_RELEASE') == '8.0.0' or \
                   current_entry.get('DISTRIB_DESCRIPTION') == '"ThinPro 8.0.0"':
                    # Print only hostname and DISTRIB_DESCRIPTION
                    print({
                        'hostname': current_entry.get('hostname'),
                        'DISTRIB_DESCRIPTION': current_entry.get('DISTRIB_DESCRIPTION')
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
                'hostname': current_entry.get('hostname'),
                'DISTRIB_DESCRIPTION': current_entry.get('DISTRIB_DESCRIPTION')
            })

# Replace 'thinpro_versions_temp.txt' with the path to your file
parse_file('thinpro_versions_temp.txt')

