# Ansible Role for Grafana

Grafana is an opensource tool for metrics visualization of some services like elasticsearch, prometheus, cloudwatch and many others. This role is written for prometheus as a datasource.

## Requirements

There is no particular requirment for running this role. As this role is platform independent for centos 6 or 7 and ubuntu 14 or 16. The only dependency for centos 6 is libselinux python and we have included that as well.
The basic requirments are:-
- Centos/Ubuntu/RedHat/Amazon-Linux Server
- Python should be installed on the target server
- 3000 port should be open in your server

## Role Variables

The role variables are defined in the [defaults](https://gitlab.com/oosm/osm_grafana/tree/master/defaults). So there is not so many variables you just have to pass the grafana version as variable.

```yaml
# vars file for grafana
grafana_version: "5.2.2"
```
You can define any type of url but for datasource name i would recommend you to go with default because the dashboards we have used is custom dashboard and there are configured for this datasource_name. Otherwise you have to add your datasource because this will not pick up the value.

Here is the list of variables and there description:-

|**Variables** | **Description** |
|--------------|-----------------|
|grafana_version | Version of grafana that you want to install |

## Dependencies

Here is the list of dependencies :-
- Port 3000 should be open on your server
- libselinux-python (Centos6)

## Example Playbook

Here is an example for the main playbook

```yaml
---
- hosts: grafana
  roles:
    - osm_grafana
```
Here We are using root as an user but you can use different user, For that you just have to make become value true. Something like this:-

```yaml
---
- hosts: grafana
  become: true
  roles:
    - osm_grafana
```

For inventory you can create a host file in which you can define your server ip, For example:-
```
[grafana]
10.1.1.100
```

You can simply use this role by using this command
```shell
ansible-playbook -i hosts site.yml
```

## Directory Structure of Role
This is the directory structure of role:-
```shell
osm_grafana
├── dashboards
│   ├── apache_exporter.json
│   ├── mongodb_exporter.json
│   ├── mysql_exporter.json
│   └── node_exporter.json
├── defaults
│   └── main.yml
├── handlers
│   └── main.yml
├── README.md
├── site.yml
├── tasks
│   ├── debian.yml
│   ├── main.yml
│   └── redhat.yml
└── templates
    └── grafana.ini.j2
```

## Dashboard Usage

If you want to use dashboards there is a [dashboards](https://gitlab.com/oosm/osm_grafana/tree/master/dashboards) directory that have some generic dashboards that you can use.

For using dashboard just paste the content of dashboard while importing dashboard in grafana.

## License

BSD

## Author Information

This role is written and maintained by [Abhishek Dubey](https://gitlab.com/abhishek-dubey). If you have any queries and sugesstion, please feel free to reach.

