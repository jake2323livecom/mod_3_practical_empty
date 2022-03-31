#!/usr/bin/env python3

# Make the necessary imports here

query_id = ''
nautobot_token = ''
devices_url = ''


headers = {}

devices = requests.get(devices_url, headers=headers, verify=False).json()['results']

hostvars = {}

groups = {
    'red_devices': {},
    'yellow_devices': {},
    'routers': {},
    'switches': {}
}

inventory = {}

# Add the hostvars and groups to your dictionary

# Print the dictionary to STDOUT