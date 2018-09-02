import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_lxd_running(host):
    service = host.service("snap.lxd.daemon")
    assert service.is_running
    assert service.is_enabled


def test_bridge(host):
    assert host.interface("br0").exists
    # Make sure the bridge interface has an IP
    assert not host.interface("br0").addresses == []


def test_bridge_is_default(host):
    with host.sudo():
        profile = host.run("lxc profile show default")
        assert profile.rc == 0
        assert "parent: br0" in profile.stdout


# Cuurently bugged.
# def test_lxd_socket_listening(host):
#    assert host.socket("tcp://0.0.0.0:8443").is_listening
#    assert host.socket("tcp://:::8443").is_listening


def test_launch_container(host):
    with host.sudo():
        host.run_test("lxc launch ubuntu:18.04 test")

        host.run_test("lxc exec test ping -c 2 google.com")

        host.run_test("lxc stop test")

        host.run_test("lxc delete test")
