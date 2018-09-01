import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_syncthing_running(host):
    service = host.service("syncthing-relay")
    assert service.is_running
    assert service.is_enabled


def test_sockets_listening(host):
    # Main sockets
    assert host.socket("tcp://0.0.0.0:22067").is_listening
    assert host.socket("tcp://:::22067").is_listening
    # Syncthing relay stats socket
    assert host.socket("tcp://0.0.0.0:22070").is_listening
    assert host.socket("tcp://:::22070").is_listening
