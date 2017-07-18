# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "debian_testing" do |debian_testing|
    debian_testing.vm.box = "fujimakishouten/debian-buster64"
    debian_testing.vm.network "private_network", ip: "192.168.33.10"
    debian_testing.vm.provision "ansible" do |ansible|
      ansible.playbook = "provision.yml"
      ansible.extra_vars = { ansible_ssh_user: 'vagrant' }
    end 
    debian_testing.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
  end

  config.vm.define "debian_stretch" do |debian_stretch|
    debian_stretch.vm.box = "debian/stretch64"
    debian_stretch.vm.network "private_network", ip: "192.168.33.11"
    debian_stretch.vm.provision "ansible" do |ansible|
      ansible.playbook = "provision.yml"
      ansible.extra_vars = { ansible_ssh_user: 'vagrant' }
    end
    debian_stretch.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
  end

  config.vm.define "ubuntu_trusty" do |ubuntu_trusty|
    ubuntu_trusty.vm.box = "ubuntu/trusty64"
    ubuntu_trusty.vm.network "private_network", ip: "192.168.33.12"
    ubuntu_trusty.vm.provision "ansible" do |ansible|
      ansible.playbook = "provision.yml"
      ansible.extra_vars = { ansible_ssh_user: 'vagrant' }
    end
    ubuntu_trusty.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
  end

  config.vm.define "ubuntu_xenial" do |ubuntu_xenial|
    ubuntu_xenial.vm.box = "ubuntu/xenial64"
    ubuntu_xenial.vm.network "private_network", ip: "192.168.33.13"
    # This box needs special handling 
    # because canonical decided the default user shouldn't be "vagrant"
    # for some retarded reason.
    ubuntu_xenial.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision.yml"
      ansible.extra_vars = { ansible_ssh_user: 'ubuntu' }
    end 
    ubuntu_xenial.vm.provider "virtualbox" do |vb|
      vb.memory = "512"
    end
  end 
end
