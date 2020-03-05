# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  config.vm.provider "virtualbox" do |vb|
    vb.memory = 2048
    vb.cpus = 1
  end

  config.vm.box = "ubuntu/xenial64"
  config.vm.box_download_insecure = true

  config.vm.define "redis-master-node" do |node|
    node.vm.hostname = "redis-master"
    node.vm.network "private_network", ip: "192.168.11.101"
    node.vm.network "forwarded_port", guest: 6379, host: 6379
    node.vm.network "forwarded_port", guest: 26379, host: 26379
  end

  config.vm.define "redis-slave1-node" do |node|
    node.vm.hostname = "redis-master"
    node.vm.network "private_network", ip: "192.168.11.111"
    node.vm.network "forwarded_port", guest: 6379, host: 6380
    node.vm.network "forwarded_port", guest: 26379, host: 26380
  end

  config.vm.define "redis-slave2-node" do |node|
    node.vm.hostname = "redis-master"
    node.vm.network "private_network", ip: "192.168.11.112"
    node.vm.network "forwarded_port", guest: 6379, host: 6381
    node.vm.network "forwarded_port", guest: 26379, host: 26381
  end

end
