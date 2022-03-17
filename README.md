# mod_3_practical

## Topics to cover:
- python
- api calls
- yaml/json
- ansible

## Build device configuration files with Ansible :D

- Clone the exam repo to your machine and go to that directory
- Create a new branch from the development branch
- Install ansible
- Complete the hosts.ini file so you can use it as an inventory source
    - Create group called 'routers'
        - Define 4 hosts:
            - router_1 with primary ip address of 1.1.1.1
            - router_2 with primary ip address of 2.2.2.2
            - router_3 with primary ip address of 3.3.3.3
            - router_4 with primary ip address of 4.4.4.4
    - Create group called 'switches'
        - Define 4 hosts
            - switch_1 with primary ip of 172.16.1.1
            - switch_2 with primary ip of 172.16.1.2
            - switch_3 with primary ip of 172.16.1.3
            - switch_4 with primary ip of 172.16.1.4
    - Define the 'all' group
        - Make the 'routers' and 'switches' groups children of 'all'

- Create the folder to store files for group variables
    - Create a file to hold variables for the group 'all'
        - You must use JSON
        - Define a variable called 'dns_servers' and set it a list of two IPs: 8.8.8.8, 8.8.4.4
    - Create a file to hold variables for the group 'routers'
        - You must use JSON
        - Define a variable called 'management_interface' and set it to 'Loopback0'
        - Define a variable called 'device_type' and set it equal to 'router'
    - Create a file to hold variables for the group 'switches'
        - Define a variable called 'management_interface' and set it to 'Vlan1000'
        - Define a variable called 'device_type' and set it equal to 'switch'

- In base.j2, fill in the empty variable call after 'hostname' on the first line

- Complete the 'physical_interfaces.j2' template to generate interface configurations
    - Using a for loop, create four physical interfaces
        - The resulting interface numbers should be 0/0, 0/1, 0/2, 0/3
        - Set the interface type to 'Ge' if the device_type is 'router', otherwise set it to 'Fe'
        - For a router, the interfaces would be Ge0/0, Ge0/1, Ge0/2, Ge0/3
        - For a switch, the interfaces would be Fe0/0, Fe0/1, Fe0/2, Fe0/3
        - For the sake of simplicity, set the ip address of each interface to 5.5.5.5 255.255.255.0

- Complete the 'dns_servers.j2' template to generate the configuration for dns servers
    - Using a for loop, create a dns configuration that includes both servers in the 'dns_servers' variable
    - example:
        - ip name-server 8.8.8.8 8.8.4.4

- Complete the 'management_interface.j2' template
    - Fill in the empty variable calls with the appropriate variables (interface name, ip address, and subnet mask)
        - The management interface's IP address should be the primary IP address of the host
        - The subnet mask should be 255.255.255.255 if the device_type is router, otherwise it should be 255.255.255.0

- Import the dns_servers.j2, physical_interfaces.j2, and management_interface.j2 templates into the base.j2 template

- Finish the playbook called build.yml
    - This playbook will generate device configuration files
    - Configure each task so that they are executed by the localhost
    - Create a 'start_time' variable equal to the current system time
    - Create a directory to store the configuration files.  The directory name should be start_time + '-configs'
        - example: '20220317182123-configs'
    - Generate device configuration files and store them in the directory you just created
        - Output to them to .cfg files
        - File name for each device should be the device hostname
        - Configure the playbook to continue if this task fails
- Run the playbook
    - Pass in an extra variable called 'syslog_server' and set the value equal to 10.10.10.10

- Commit the changes to your branch

