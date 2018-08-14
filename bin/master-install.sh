#!/usr/bin/env sh
# This script provisions a new ansible master.

test -e /usr/bin/ansible || (sudo apt -y update && sudo apt install software-properties-common && sudo apt-add-repository ppa:ansible/ansible && sudo apt update && sudo apt install -y ansible)
