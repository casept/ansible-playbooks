# My ansible playbooks for setting up machines

These are my private ansible playbooks and related files, mostly to set up my workstations.
They're tailored only to my needs, so distros other than ubuntu are untested (and non-deb based ones won't work).

## Installation

```shell
git clone --recursive https://github.com/casept/ansible-playbooks
cd ansible-playbboks
# Edit the vars/devbox.yml file to your liking (Important! If you don't do this you'll get my SSH public key installed onto your box!)
bin/devbox
```
