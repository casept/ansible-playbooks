# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define "ubuntu_bionic" do |ubuntu_bionic|
    ubuntu_bionic.vm.box = "ubuntu/bionic64"
    ubuntu_bionic.vm.provision "ansible" do |ansible|
      ansible.playbook = "roles/raw-python/tasks/main.yml"
    end
  end
  config.vm.define "debian_stretch" do |debian_stretch|
    debian_stretch.vm.box = "debian/contrib-stretch64"
    # Just used to get an inventory file
    debian_stretch.vm.provision "ansible" do |ansible|
      ansible.playbook = "roles/raw-python/tasks/main.yml"
    end
  end
  config.vm.define "debian_sid" do |debian_sid|
    debian_sid.vm.box = "bluehorn/debian-sid64"
    # Just used to get an inventory file
    debian_sid.vm.provision "ansible" do |ansible|
      ansible.playbook = "roles/raw-python/tasks/main.yml"
    end
  end
end
