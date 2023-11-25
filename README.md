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

ssh_key_management.yml - Manages SSH keys for secure access to Thin Clients.

ping_servers.yml - Checks network connectivity by pinging servers.

uptime.yml - Reports the uptime of Thin Clients.

An inventory file is also included to manage the list of HP Thin Clients.



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

Contributing

Contributions are welcome. Please adhere to the following guidelines:

Fork the repository and create a branch for your feature or fix.
Ensure code adherence to the existing style and standards.
Submit a pull request with a clear description of changes.
License

[Specify the license here, or state "This project is licensed under the MIT License - see the LICENSE file for details"]

This updated README now includes the specific directory paths for both environments. You can further modify it to suit any additional details or requirements of your project.
