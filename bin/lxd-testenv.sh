#!/usr/bin/env bash
# This script sets up a test environment using LXD containers.
# These containers can be used for testing playbooks more rapidly because they don't require
# waiting for an entire VM to boot.
# Vagrant isn't used because setting up the LXD provider is tricky and few boxes support it.


# The containers are created on the host using an ansible playbook,
# and destroyed using a different playbook.
if [[ $1 == "create" ]]; then
	ansible-playbook testcontainers-create.yml
fi

if [[ $1 == "destroy" ]]; then
	ansible-playbook testcontainers-destroy.yml
fi
