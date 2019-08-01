import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_grafana_is_installed(host):
    grafana = host.package("grafana")
    assert grafana.is_installed


def test_config_file(host):
    f = host.file('/etc/grafana/grafana.ini')
    assert f.exists
    assert f.is_file


def test_grafana_dashboard_dir(host):
    d = host.file('/var/lib/grafana/dashboards')
    assert d.exists
    assert d.is_directory
    assert d.user == "grafana"
    assert d.group == "grafana"
    assert d.mode == '0755'


def test_grafana_running_and_enabled(host):
    os = host.system_info.distribution
    if os == '16':
        grafana = host.service("grafana-server")
        assert grafana.is_running
        assert grafana.is_enabled
    if os == '7':
        grafana = host.service("grafana-server")
        assert grafana.is_running
        assert grafana.is_enabled


def test_grafana_is_listening(host):
    assert host.socket('tcp://127.0.0.1:3000').is_listening
