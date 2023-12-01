# hp-thin-client-upgrade

HP Thin Client Upgrade Automation with Ansible

This repository contains Ansible playbooks for automating the upgrade of approximately 8500 HP Thin Client devices from HP ThinPro versions 7.0 and 7.1 to version 8.0.

Overview

The primary execution environment for these playbooks is a dedicated Red Hat Ansible server (IDCPLADMIN01, IP: 172.23.7.244). They can also be executed from macOS devices as a secondary option or for backup purposes.


Directory Structure

On the Red Hat server: /home/[username]/Ansible_Playbooks

On macOS: /Users/[username]/Ansible_Playbooks
Replace [username] with your actual username on the respective systems.


Playbooks

This project includes the following Ansible playbooks:

backup_store_printers_conf.yml - Backs up printer configurations from the HP Thin Clients.

deploy_printers_conf_to_stores.yml - Deploys printer configurations to stores.

get_thinpro_os_version.yml - Gathers the Thin Pro system versions from HP ThinPro devices.

ssh_key_management.yml - Manages SSH keys for secure access to Thin Clients.

ping_servers.yml - Checks network connectivity by pinging servers.

uptime.yml - Reports the uptime of Thin Clients.

An inventory file is also included to manage the list of HP Thin Clients.




Python Scripts for Enhanced Management

In addition to the Ansible playbooks, this repository includes two Python scripts designed to further streamline the management and analysis of HP Thin Client devices.

ThinPro Version Parser (ThinProVersionParser.py)

Description: This script is tailored for parsing a file containing entries of ThinPro systems, specifically identifying and processing entries with version 8.0.0. It reads through a file, identifies each system entry, and extracts relevant details like hostname and distribution description for systems matching the specified version.

Usage: (tmp/thinpro_versions_file.txt') 

ThinPro Inventory Creator (ThinProInventoryCreator.py)

Description: This script automates the generation of an Ansible-compatible inventory list from a dataset of ThinPro systems. It processes each system's hostname and IP address, creating a formatted inventory line including the Ansible user (set to 'root') for each ThinPro system in the dataset.

Usage: Supply the script with a dataset of ThinPro system details. It outputs a ready-to-use inventory list for Ansible, enhancing automation efficiency.


Example:

data = [
    {'hostname': 'WS5002-TC02 - IP: 10.131.194.213', 'DISTRIB_DESCRIPTION': '"ThinPro 8.0.0"'},
    # ... (additional entries)
]

inventory = create_inventory(data)
for line in inventory:
    print(line)
These scripts are integral for efficient ThinPro system management, especially when dealing with large networks of devices.




Getting Started

Prerequisites
Ansible 2.9 or higher installed on the Red Hat server or macOS.
SSH access to the Thin Clients.
Network access to the HP Thin Client environment.
Installing Ansible on MacOS
For backup or supplementary use, Ansible can be installed on macOS:

Install Homebrew (if not already installed):

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install Ansible using Homebrew:

brew install ansible

Verify the installation:

ansible --version

Running the Playbooks
On the Red Hat Ansible Server
Navigate to the playbook directory and run:

ansible-playbook <playbook-name>.yml -i inventory

On MacOS
Change to the playbook directory on your Mac and run:

ansible-playbook <playbook-name>.yml -i inventory
Replace <playbook-name> with the specific playbook you wish to execute.

Contributions are welcome. Please adhere to the following guidelines:

Fork the repository and create a branch for your feature or fix.
Ensure code adherence to the existing style and standards.
Submit a pull request with a clear description of changes.

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details
