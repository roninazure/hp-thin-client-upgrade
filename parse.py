# Script Name: ThinProInventoryCreator.py
# Description: This script generates an Ansible inventory list from a given dataset 
#              of ThinPro systems. Each system is represented by its hostname, IP address,
#              and a predefined ansible_user (root).
# Input: A list of dictionaries, where each dictionary contains 'hostname' and 
#        'DISTRIB_DESCRIPTION' keys. The hostname includes the system name and IP address.
# Output: Generates and prints an inventory list formatted for use with Ansible, 
#         which includes the hostname, IP address, and ansible_user for each entry.

data = [
    {'hostname': 'WS5002-TC02 - IP: 10.131.194.213', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5002-TC06 - IP: 10.131.194.217', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5005-TC02 - IP: 10.131.195.217', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5005-TC04 - IP: 10.131.195.221', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5005-TC06 - IP: 10.131.195.206', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5010-TC02 - IP: 10.130.201.210', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5010-TC04 - IP: 10.130.201.216', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5010-TC06 - IP: 10.130.201.218', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5017-TC02 - IP: 10.130.200.208', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5017-TC04 - IP: 10.130.200.209', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5017-TC06 - IP: 10.130.200.213', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5022-TC02 - IP: 10.130.226.222', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5022-TC04 - IP: 10.130.226.219', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5022-TC06 - IP: 10.130.226.218', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5024-TC02 - IP: 10.130.206.214', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5024-TC04 - IP: 10.130.206.203', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5024-TC06 - IP: 10.130.206.208', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5216-TC02 - IP: 10.130.207.218', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5216-TC04 - IP: 10.130.207.209', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    {'hostname': 'WS5216-TC06 - IP: 10.130.207.203', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
]

def create_inventory(data):
    inventory = []
    for entry in data:
        # Split the hostname and IP address
        parts = entry['hostname'].split(' - IP: ')
        hostname = parts[0].rstrip(':')
        ip_address = parts[1].rstrip(':')
        inventory_line = f"{hostname} ansible_host={ip_address} ansible_user=root"
        inventory.append(inventory_line)

    return inventory

inventory = create_inventory(data)
for line in inventory:
    print(line)

