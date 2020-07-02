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

input_parameter_path = path + '/' + "input_parameter_regist.json"

# Load json file
with open(input_parameter_path) as file_object:
    input_parameter = file_object.read()
parameter = json.loads(input_parameter)

result['VAR_Zabbix40AG_serverregist'] = parameter['VAR_Zabbix40AG_serverregist']
result['VAR_Zabbix40AG_APITempPath'] = parameter['VAR_Zabbix40AG_APITempPath']
result['VAR_Zabbix40AG_Username'] = parameter['VAR_Zabbix40AG_Username']
result['VAR_Zabbix40AG_Password'] = parameter['VAR_Zabbix40AG_Password']
result['VAR_Zabbix40AG_ServerAddress'] = parameter['VAR_Zabbix40AG_ServerAddress']
if parameter['VAR_Zabbix40AG_Hostname'] == "":
    result['VAR_Zabbix40AG_Hostname'] = "{{ ansible_hostname }}"
else:
    result['VAR_Zabbix40AG_Hostname'] = parameter['VAR_Zabbix40AG_Hostname']

result['VAR_Zabbix40AG_DisplayName'] = parameter['VAR_Zabbix40AG_DisplayName']
if parameter['VAR_Zabbix40AG_HostIP'] == "":
    result['VAR_Zabbix40AG_HostIP'] = "{{ ansible_host }}"
else:
    result['VAR_Zabbix40AG_HostIP'] = parameter['VAR_Zabbix40AG_HostIP']

result['VAR_Zabbix40AG_AgentPort'] = parameter['VAR_Zabbix40AG_AgentPort']
result['VAR_Zabbix40AG_SnmpPort'] = parameter['VAR_Zabbix40AG_SnmpPort']

result['VAR_Zabbix40AG_HostGroups'] = []
temp = str(parameter['VAR_Zabbix40AG_HostGroups'])  # [u'test_zabbix', u'linux_zabbix']
for index in range(len(temp.split("'"))):           # ['[u', 'test_zabbix', ', u', 'linux_zabbix', ']']
    if index % 2 == 1:
        result['VAR_Zabbix40AG_HostGroups'].append(temp.split("'")[index])

result['VAR_Zabbix40AG_Templates'] = []
temp = str(parameter['VAR_Zabbix40AG_Templates'])   # [u'test_zabbix', u'linux_zabbix']
for index in range(len(temp.split("'"))):           # ['[u', 'test_zabbix', ', u', 'linux_zabbix', ']']
    if index % 2 == 1:
        result['VAR_Zabbix40AG_Templates'].append(temp.split("'")[index])

print(json.dumps(result))
