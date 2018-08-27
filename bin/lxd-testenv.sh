#!/usr/bin/env bash
# This script sets up a test environment using LXD containers.
# These containers can be used for testing playbooks more rapidly because they don't require
# waiting for an entire VM to boot.
# Vagrant isn't used because setting up the LXD provider is tricky and few boxes support it.


# The containers are created on the host using an ansible playbook,
# and destroyed using a different playbook.


function create {
	ansible-playbook -i inventory/lxd-testenv testcontainers-create.yml
}

function destroy {
	ansible-playbook -i inventory/lxd-testenv testcontainers-destroy.yml
}

function recreate {
	destroy
	create
}

function usage {
	echo "Usage: $0 [create|destroy|recreate]"
	exit 1
}

if [ "$1" != "create" ] && [ "$1" != "destroy" ] && [ "$1" != "recreate" ]; then
	usage "$@"
fi

if [[ $1 == "create" ]]; then
	create
fi

if [[ $1 == "destroy" ]]; then
	destroy
fi

if [[ $1 == "recreate" ]]; then
	recreate
fi
