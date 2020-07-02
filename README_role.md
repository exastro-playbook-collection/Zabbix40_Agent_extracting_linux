# Zabbix Agent Ver4.0 (Linux) パラメータ生成ロール

# Trademarks
-----------
* Linuxは、Linus Torvalds氏の米国およびその他の国における登録商標または商標です。
* RedHat、RHEL、CentOSは、Red Hat, Inc.の米国およびその他の国における登録商標または商標です。
* Windows、PowerShellは、Microsoft Corporation の米国およびその他の国における登録商標または商標です。
* Ansibleは、Red Hat, Inc.の米国およびその他の国における登録商標または商標です。
* pythonは、Python Software Foundationの登録商標または商標です。
* Zabbixは、ラトビア共和国にあるZabbix LLCの商標です。
* Oracleは、Oracle International Corporation の米国およびその他の国における登録商標または商標です。
* NECは、日本電気株式会社の登録商標または商標です。
* その他、本ロールのコード、ファイルに記載されている会社名および製品名は、各社の登録商標または商標です。

## Description

本ロールでは、Zabbix Agent Ver4.0 Linux版構築済み環境から設定情報を収集する機能と、収集した設定情報からZabbix Agent Ver4.0 Linux版構築ロール(Zabbix-agent_Ver4.0)で使用できるパラメータを生成する機能を提供します。

## Supports

本ロールは、以下環境をサポートします。

- 管理サーバー（Ansible実行サーバー）
  - OS：RHEL7.4（CentOS7.4）/RHEL8.0（CentOS8.0）
  - Ansible：Version 2.8
  - Python：2.7 or 3.6
- 対象サーバー
  - 利用しているロール、共通部品の仕様に準拠します。

## Dependencies

本ロールでは、以下のロール、共通部品を利用しています。

- 収集機能（Zabbix40_Agent_gathering_linux）
  - gathering ロール
- パラメータ生成機能（Zabbix40_Agent_extracting_linux）
  - パラメータ生成共通部品

## Role Variables

本ロールで指定できる変数値について説明します。

### Mandatory Variables

ロール利用時に必ず指定しなければならない変数値はありません。

### Optional Variables

ロール利用時に以下の変数値を指定することができます。

- 共通

    | Name                            | Default Value | Description                        |
    | ------------------------------- | ------------- | -----------------------------------|
    |`VAR_Zabbix_Agent_gathering_dest`|'{{ playbook_dir }}_gathered_data' |収集した設定情報の格納先パス |

- Zabbix40_Agent_gathering_linux

    | Name                            | Default Value | Description                        |
    | ------------------------------- | ------------- | -----------------------------------|
    |`VAR_Zabbix40AG_DestPathName`    |'/tmp/zabbix_agent'                |構築対象サーバ上のZabbixリポジトリパッケージファイル「zabbix-relaese-3.5-1.el6.noarch.rpm」(RHEL6)または、「zabbix-relaese-3.5-1.el7.noarch.rpm」のコピー先フォルダ  |
    |`VAR_Zabbix40AG_serverregist`    |"yes"                              |サーバへの登録  |
    |`VAR_Zabbix40AG_APITempPath`     |'/tmp/zbx_api'                     |作業用パス  |
    |`VAR_Zabbix40AG_Username`        |'Admin'                            |Zabbixサーバへのログイン名  |
    |`VAR_Zabbix40AG_Password`        |'zabbix'                           |Zabbixサーバへのログインパスワード  |
    |`VAR_Zabbix40AG_Server`          |'192.168.1.1'                      |ZabbixサーバのIPアドレス  |
    |`VAR_Zabbix40AG_ServerAddress`   |'http://192.168.1.1:80/zabbix/'    |ZabbixサーバAPIへのアドレス  |
    |`VAR_Zabbix40AG_Hostname`        |'{{ ansible_hostname }}'           |ホスト名  |
    |`VAR_Zabbix40AG_DisplayName`     |''                                 |ホスト表示名  |
    |`VAR_Zabbix40AG_HostIP`          |'{{ ansible_host }}'               |ホストIPアドレス  |
    |`VAR_Zabbix40AG_AgentPort`       |'10050'                            |エージェントポート番号  |
    |`VAR_Zabbix40AG_SnmpPort`        |'161'                              |SNMPポート番号  |
    |`VAR_Zabbix40AG_HostGroups`      |['test_zabbix','linux_zabbix',"zabbix"]    |ホストが属するホストグループ  |
    |`VAR_Zabbix40AG_Templates`       |['Template OS Linux']              |ホストへリンクするTemplate名  |

- Zabbix40_Agent_extracting_linux

    | Name                             | Default Value                    | Description      |
    | -------------------------------- | -------------------------------- | -----------------|
    |`VAR_Zabbix_Agent_extracting_rolename`  |'['Zabbix40-Agent_install','Zabbix40-Agent_setup','Zabbix40-Agent_regist']'  |パラメータ生成対象  |
    |`VAR_Zabbix_Agent_extracting_dest`  |'{{ playbook_dir }}/_parameters'     |生成したパラメータファイルの格納先パス  |

## Results

本ロールの出力について説明します。

### 収集した設定情報の格納先

収集した設定情報は以下のディレクトリ配下に格納します。

- {{ VAR_Zabbix_Agent_gathering_dest }}/<ホスト名/IP>/Zabbix40_Agent_gathering_linux/

本ロールをデフォルト設定で利用した場合、以下のように設定情報を格納します。
- Zabbix Agent(Linux版) Ver4.0 の場合

    ```none
    <Playbook実行ディレクトリ>/
      +-_gathered_data/
          +-<ホスト名/IP>/
              +-Zabbix40_Agent_gathering_linux/                      # 収集データ
                  +-commond/
                        ：
    ```

### 生成したパラメータの出力例

生成したパラメータは以下のディレクトリ・ファイル名で出力します。

- {{ VAR_Zabbix_Agent_extracting_dest }}/<ホスト名/IP>/{{ VAR_Zabbix_Agent_extracting_rolename }}.yml

本ロールをデフォルト設定で利用した場合、以下のようにパラメータを出力します。

- Zabbix Agent(Linux版) Ver4.0 の場合

    ```none
    <Playbook実行ディレクトリ>/
      +-_parameters/
          +-<ホスト名/IP>/
			  +-Zabbix40-Agent_install.yml               # パラメータ
			  +-Zabbix40-Agent_setup.yml                 # パラメータ
			  +-Zabbix40-Agent_regist.yml                # パラメータ
    ```

## Usage

本ロールの利用例について説明します。

### 設定情報収集およびパラメータ生成を行う場合

以下の例ではデフォルト設定で設定情報収集およびパラメータ生成を行います。
- `Zabbix40_Agent_linux_pargen.yml` (Linux版Zabbix Agent Ver4.0用Playbook)

    ```yaml
    ---
      - hosts: all
        gather_facts: true
        roles:
          - role: Zabbix40_Agent_gathering_linux

      - hosts: all
        gather_facts: no
        roles:
          - role: Zabbix40_Agent_extracting_linux
    ```

- 以下のように設定情報とパラメータを出力します。

    ```none
    <Playbook実行ディレクトリ>/
      +-_gathered_data/
      |   +-<ホスト名/IPアドレス>/
      |       +-Zabbix40_Agent_gathering_linux/              # 収集データ
      |           +-commond/
      |               ：
      +-_parameters/
          +-<ホスト名/IPアドレス>/
			  +-Zabbix40-Agent_install.yml                   # パラメータ
			  +-Zabbix40-Agent_setup.yml                     # パラメータ
			  +-Zabbix40-Agent_regist.yml                    # パラメータ
    ```

### パラメータ再利用

以下の例では、生成したパラメータを使用して構築済Zabbix Agent Ver4.0の設定を変更します。

- `Zabbix40-Agent_setup-playbook.yml`（Linux版Zabbix Agent Ver4.0構築ロールを使用）

    ```yaml
    ---
    - hosts: Zabbix
      become: yes
      roles:
        - Zabbix40-Agent_setup
    ```

- 生成したパラメータを指定してplaybookを実行

    ```sh
    ansible-playbook Zabbix40-Agent_setup-playbook.yml -i hosts --extra-vars="@_parameters/<ホスト名/IPアドレス>/Zabbix40-Agent_setup.yml"
    ```

# Copyright
Copyright (c) 2019 NEC Corporation

# Author Information
NEC Corporation
