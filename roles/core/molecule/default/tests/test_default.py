import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

users = ["maintenance", "ansible"]


def test_users_present(host):
    for username in users:
        user = host.user(username)
        assert "nopasswders" in user.groups


def test_ssh_directory_perms(host):
    for username in users:
        ssh_dir = host.file("/home/{0}/.ssh".format(username))
        assert ssh_dir.is_directory
        assert ssh_dir.user == username
        assert ssh_dir.group == username
        assert ssh_dir.mode == 0o700


def test_ssh_authorized_keys_perms(host):
    for username in users:
        with host.sudo(username):
            authorized_keys = host.file(
                "/home/{0}/.ssh/authorized_keys".format(username))
            assert authorized_keys.is_file
            assert authorized_keys.user == username
            assert authorized_keys.group == username
            assert authorized_keys.mode == 0o600


def test_ssh_keys_present(host):
    ssh_keys = ["ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDPI1AD5QDRLDrewxCIeYrrtjfUNSZvzm+jqmchiwjiXsoTtUbc1b4kGBeOxy8aVQ6ho7LwTw6fVQQcABAYmaFkLJK3GZF7izrN6QQ0VmjjJgVq8dhwMwU4WQL1W69nWeRx/MaWlil3my5YNQVZVglHZbjIFdnbXWWRhMdb16XQLMgPJpQFPoW8fV8D8ubtg/GrBCJNikEflRzcDLvx5eqF0Jmph9QUiRH1LoGi5hRlD+TIkitPSsItbecJ38mUlIdunl3xcuv0iHkP4e5T4AwRgkqmnAA8RSKQ6rnyXAk0dIpHXWcOIJeFU+5Klok3TZogudQhb2MkLdEqHUxWpmd9 root@57cfb02cb2ab",  # noqa: E501
            "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC5aJzaZDaiwgWs1TTYiGesAlV1Z11pZAMz9Lg2R9JS74chq1+OaFrbMABwZUp3BaFE/KpQHY1fBPGZuZERiYkI4HB5swtPtZo55mkEdPiqEH+TmdiqMLZDlr1G3IkcPu5mvWEZyrTAXcvw9nb/pDkcdT9pxWkMzG+kdWqJuqdlzGukH6mO1+tCezy8LXcEZ2AmmbHMMnSV6RTP2C+JRMaltAmF55cL4uwPxNhXr8iFT00i6NTPjaIfdg6lH7qxeddFEZ+115DUnpESipoE9xQjYtA/8T8fw6WmxgO9xsbAnQDUoQMdwdg07lAJ6BhfomTMTk4Y+PXumf3yIo0bpos7 root@57cfb02cb2ab"]  # noqa: E501
    for username in users:
        with host.sudo(username):
            authorized_keys_file = host.file(
                "/home/{0}/.ssh/authorized_keys".format(username))
            for key in ssh_keys:
                assert key in authorized_keys_file.content_string


def test_ssh_service_running(host):
    sshd = host.service("ssh")
    assert sshd.is_running
    assert sshd.is_enabled


def test_mosh_installed(host):
    assert host.package("mosh").is_installed


def test_hostname_changed(host):
    cmd = host.run("hostname")
    assert cmd.rc == 0
    assert cmd.stdout == "testhost"
