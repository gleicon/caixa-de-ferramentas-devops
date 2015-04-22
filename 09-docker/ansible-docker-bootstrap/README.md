# docker for ubuntu

## Install on VPS/VM/Cloud
    
    - Create or add your hostnames into the inventory
        [servers]
        hostname 

    - SSH keys must works, adjust docker.yml with your username
    - Run 
        ansible-playbook -i inventory.ini docker.yml

## Run on Vagrant
   - vagrant up
   - vagrant ssh

## What you get
    - Ubuntu 14.04 64 bits
    - Latest Docker
    - Nginx
    - Python and build packages

## Built on
    - https://github.com/bennojoy/nginx
    - https://github.com/angstwad/docker.ubuntu
    - Ansible
    - Vagrant
