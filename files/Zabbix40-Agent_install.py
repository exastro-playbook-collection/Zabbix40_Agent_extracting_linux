# -*- coding: UTF-8 -*-
import re
import json
import sys
import os

# main process
args = sys.argv

if (len(args) < 2):
    sys.exit(1)

path = args[1]
if(path[-1:] == "/"):
    path = path[:-1]
result = {}

input_parameter_path = path + '/' + "input_parameter_install.json"

# Load json file
with open(input_parameter_path) as file_object:
    input_parameter = file_object.read()
parameter = json.loads(input_parameter)

zabbix_pkglist=['zabbix-agent','zabbix-sender','zabbix-get']

result['VAR_Zabbix40AG_DestPathName'] = parameter['VAR_Zabbix40AG_DestPathName']
result['VAR_Zabbix40AG_RepoPKG_el7'] = 'zabbix-release-4.0-1.el7.noarch.rpm'
result['VAR_Zabbix40AG_PKGlist'] = zabbix_pkglist
print(json.dumps(result))
