# -*- mode: ruby -*-
# vi: set ft=ruby :
#
# Setup: Install Vagrant, cd to this directory, and run
#
# ./scripts/deeprotor setup

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  config.disksize.size='50GB'

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 8192
    vb.cpus = 4
  end

  config.vm.provision "deps", type: "shell", inline: <<-SHELL
    apt-get update
    apt-get install -y lxqt xinit ntp
    echo "Reboot to start using UI"
  SHELL

  config.vm.provision "env", type: "shell", privileged: false, inline: <<-SHELL
    /vagrant/scripts/deeprotor setup && echo "deeprotor cd" >> ~/.bashrc
  SHELL
end
