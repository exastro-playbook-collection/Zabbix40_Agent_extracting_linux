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
zab_conf_path = path + '/command/0/stdout.txt'
zab_sta_path = path + '/command/2/stdout.txt'
zab_isenable_path = path + '/command/3/stdout.txt'


# For parameter VAR_Zabbix40AG_start
if os.path.isfile(zab_sta_path):
    with open(zab_sta_path) as file_object:
        zab_sta_lines = file_object.readlines()
    for line in zab_sta_lines:
        line = line.strip()
        if line == "":
            continue
        if "Active" in line and "running" in line:
            VAR_Zabbix40AG_start = 'yes'
            break
        else:
            VAR_Zabbix40AG_start = 'no'

# For parameter VAR_Zabbix40AG_chkconfig
if os.path.isfile(zab_isenable_path):
    with open(zab_isenable_path) as file_object:
        zab_isenable_lines = file_object.readlines()
    for line in zab_isenable_lines:
        line = line.strip()
        if line == "":
            continue
        if line.split()[1] == "enabled" :
            VAR_Zabbix40AG_chkconfig = 'on'
        else:
            VAR_Zabbix40AG_chkconfig = 'off'

# Filter specified entries for key-value
def functionname( para_name, content_name, line):
    if (re.match( '\s*' + content_name + '\s*=\s*(.*)', line) != None):
        temp_var = line.split('=')[1].strip()
        result[para_name] = temp_var

# Filter specified entries for key-list
def functionname_list( para_name, content_name, line):
    if (re.match( '\s*' + content_name + '\s*=\s*(.*)', line) != None):
        temp_var = line.split('=')[1].strip()
        if not para_name in result:
            result[para_name]=[]
        result[para_name].append(temp_var)

zabbix_conf_dict={
    'VAR_Zabbix40AG_LogType':'LogType',
    'VAR_Zabbix40AG_LogFile':'LogFile',                 #Must be defined
    'VAR_Zabbix40AG_LogFileSize':'LogFileSize',         #Must be defined
    'VAR_Zabbix40AG_DebugLevel':'DebugLevel',
    'VAR_Zabbix40AG_SourceIP':'SourceIP',
    'VAR_Zabbix40AG_EnableRemoteCommands':'EnableRemoteCommands',
    'VAR_Zabbix40AG_LogRemoteCommands':'LogRemoteCommands',
    'VAR_Zabbix40AG_Server':'Server',
    'VAR_Zabbix40AG_ListenPort':'ListenPort',
    'VAR_Zabbix40AG_ListenIP':'ListenIP',
    'VAR_Zabbix40AG_StartAgents':'StartAgents',
    'VAR_Zabbix40AG_ServerActive':'ServerActive',       #Must be defined
    'VAR_Zabbix40AG_Hostname':'Hostname',               #Must be defined
    'VAR_Zabbix40AG_HostnameItem':'HostnameItem',
    'VAR_Zabbix40AG_HostMetadata':'HostMetadata',
    'VAR_Zabbix40AG_HostMetadataItem':'HostMetadataItem',
    'VAR_Zabbix40AG_RefreshActiveChecks':'RefreshActiveChecks',
    'VAR_Zabbix40AG_BufferSend':'BufferSend',
    'VAR_Zabbix40AG_BufferSize':'BufferSize',
    'VAR_Zabbix40AG_MaxLinesPerSecond':'MaxLinesPerSecond',
    'VAR_Zabbix40AG_Timeout':'Timeout',
    'VAR_Zabbix40AG_AllowRoot':'AllowRoot',
    'VAR_Zabbix40AG_User':'User',
    'VAR_Zabbix40AG_UnsafeUserParameters':'UnsafeUserParameters',
    'VAR_Zabbix40AG_LoadModulePath':'LoadModulePath',
    'VAR_Zabbix40AG_TLSConnect':'TLSConnect',
    'VAR_Zabbix40AG_TLSAccept':'TLSAccept',
    'VAR_Zabbix40AG_TLSCAFile':'TLSCAFile',
    'VAR_Zabbix40AG_TLSCRLFile':'TLSCRLFile',
    'VAR_Zabbix40AG_TLSServerCI':'TLSServerCertIssuer',
    'VAR_Zabbix40AG_TLSServerCS':'TLSServerCertSubject',
    'VAR_Zabbix40AG_TLSCertFile':'TLSCertFile',
    'VAR_Zabbix40AG_TLSKeyFile':'TLSKeyFile',
    'VAR_Zabbix40AG_TLSPSKId':'TLSPSKIdentity',
    'VAR_Zabbix40AG_TLSPSKFile':'TLSPSKFile'
    }

zabbix_conf_list_dict={
    'VAR_Zabbix40AG_Alias':'Alias',
    'VAR_Zabbix40AG_Include':'Include',
    'VAR_Zabbix40AG_UserParameter':'UserParameter',
    'VAR_Zabbix40AG_LoadModule':'LoadModule'
    }

# For parameter in zabbix-agentd.conf
if os.path.isfile(zab_conf_path):
    with open(zab_conf_path) as file_object:
        zab_conf_lines = file_object.readlines()
    for line in zab_conf_lines:
        line = line.strip()
        for temp in zabbix_conf_dict.keys():
            functionname(temp,zabbix_conf_dict[temp],line)
        for var in zabbix_conf_list_dict.keys():
            functionname_list(var,zabbix_conf_list_dict[var],line)

result['VAR_Zabbix40AG_start'] = VAR_Zabbix40AG_start
result['VAR_Zabbix40AG_chkconfig'] = VAR_Zabbix40AG_chkconfig

print(json.dumps(result))
