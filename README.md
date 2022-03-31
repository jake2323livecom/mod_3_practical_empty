# mod_3_practical

## Topics to cover:
- python
- api calls
- yaml/json
- ansible

## Build device configuration files with Ansible

- Clone the exam repo to your machine and go to that directory
- Create a new branch from the development branch
- Install ansible
- Using ansible-galaxy, install the netcommon collection
- Configure the ansible config file to allow inventory scripts to be used as inventory sources
- Finish the 'inventory.py' dynamic inventory file

    - Use an API call to nautobot to pull info for all devices that belong to the site 'orko' in Nautobot

    - Using the information returned from the API call:

        - Create the hostvars section of the inventory
            - Each device should have two variables:
                - ansible_host
                - device_type

        - Create all necessary groups and add them to the inventory
            - Create a group of devices that have the platform 'red' and name the group 'red_devices'
            - Create a group of devices that have the platform 'yellow' and name the group 'yellow_devices'
            - Create a group of devices that have the device_role 'router' and name the group 'routers'
            - Create a group of devices that have the device_role 'switch' and name the group 'switches'

    - Print the inventory to STDOUT in JSON format

- Create a folder to store files for group variables

    - Create a JSON file for the 'red_devices' group 
        - Define a variable called 'dns_servers' and set it to this list of IPs: 10.10.20.98, 10.10.20.99

    - Create a JSON file for the 'yellow_devices' group
        - Define a variable called 'dns_servers' and set it to this list of IPs: 10.10.30.98, 10.10.30.99

    - Create a JSON file for the 'routers' group
        - Define a variable called 'management_interface' and set it to 'Loopback0'

    - Create JSON file for the 'switches' group
        - Define a variable called 'management_interface' and set it to 'Vlan1000'

- In base.j2, fill in the empty variable call after 'hostname' on the first line using an ansible special variable

- Finish the 'physical_interfaces.j2' template to generate the configuration for all physical interfaces
    - Loop through the 'interfaces' variable defined in the 'all.json' group_vars file
    - Configure each interface's IP address and subnet mask
        - Use the appropriate data from the 'interfaces' variable

- Finish the 'dns_servers.j2' template to generate the dns server configuration
    - Loop through the 'dns_servers' variable
    - example:
        - ip name-server 8.8.8.8 8.8.4.4

- Finish the 'management_interface.j2' template
    - Fill in the empty variable calls with the appropriate variables
        - The management interface's IP address should be the primary IP address of the host
        - Use a ternary variable assignment to determine the subnet mask
            - It should be '255.255.255.255' if the device_type is 'router', else set it to '255.255.255.0'

- Import the dns_servers.j2, physical_interfaces.j2, and management_interface.j2 templates into the base template

- Finish the playbook called build.yml
    - Ensure necessary tasks are carried out by the localhost
    - The playbook should have 6 tasks:
        - Create the 'start_time' variable and set the value to the current system time
        - Create a directory to store device config files
            - Make sure the new directory is a sub-directory of the playbooks directory
            - Use the 'start_time' variable in the name
            - Example: playbooks/20210101010101-configs/
        - Generate device config files and store in the directory you created
            - Output the files in a .cfg format
            - Each device's config file should have it's hostname in the name of the file
            - Set the playbook to continue if the config generation fails for any one device
        - Use scp to send configs to their respective devices
        - Send a command to each device telling it to restart
        - Delete the directory you created

- Run the playbook
    - Pass in an extra variable called syslog_server and set the value equal to 10.10.10.10
    
- Commit the changes to your branch

