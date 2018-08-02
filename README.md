# Ansible Role for Grafana

Grafana is an opensource tool for metrics visualization of some services like elasticsearch, prometheus, cloudwatch and many others. This role is written for prometheus as a datasource

## Requirements

There is no particular requirment for running this role. As this role is platform independent for centos 6 or 7 and ubuntu 14 or 16. The only dependency for centos 6 is libselinux python and we have included that as well.
The basic requirments are:-
- Centos/Ubuntu Server
- Python should be installed on the target server
- 3000 port should be open in your server

## Role Variables
The role variables are defined in the [vars](https://gitlab.com/oosm/osm_grafana/tree/master/vars). So there is not so many variables you just have to pass the datasource name and datasource url in the variable.

```yaml
# vars file for grafana
datasource_name: "prometheus.internal-odmont.com"
datasource_url: "http://prometheus:9090"
```
You can define any type of url but for datasource name i would recommend you to go with default because the dashboards we have used is custom dashboard and there are configured for this datasource_name. Otherwise you have to add your datasource because this will not pick up the value

## Dependencies

There is no further dependency for this role you just need prometheus installed on any server and pass that url in variabled so that grafana can pull metrics from there

## Example Playbook

Here is an example for the main playbook

```yaml
---
- hosts: grafana
  user: root
  roles:
    -  grafana
```
Here We are using root as an user but you can use different user, For that you just have to make become value true. Something like this:-
```yaml
---
- hosts: grafana
  user: test-user
  become: true
  roles:
    -  grafana
```
You can simply use this role by using this command
```shell
ansible-playbook -i hosts site.yml
```
## License

BSD

## Author Information

This role is written and maintained by [Abhishek Dubey](https://gitlab.com/abhishek-dubey). If you have any queries and sugesstion, please feel free to reach.
