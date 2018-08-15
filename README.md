# My ansible playbooks

These are my private ansible playbooks and related files for setting up my machines.
They're tailored only to my needs, so distros other than ubuntu bionic are untested (and non-deb based ones won't work).

## Installation

```shell
git clone --recursive https://github.com/casept/ansible-playbooks
cd ansible-playbooks
# The plays are in the root directory.
# core.yml does everything needed to prepare a host for other plays, so run that first.
# Remember to replace my SSH keys in vars/ssh_keys.yml with your own.
```
