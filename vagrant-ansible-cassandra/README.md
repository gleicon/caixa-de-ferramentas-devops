# Vagrant + Ansible + Cassandra

Este playbook instala o Cassandra em três modalidades:
	
	- Vagrant
	- Máquinas existentes
	- EC2

Este playbook configura parâmetros simples como o nome do cluster, tipo de Snitch, seeds, listen e rpc address.

[cassandra]
192.168.33.100 cluster_name="Super Cluster" seeds="192.168.33.100,192.168.33.101,192.168.33.102" listen_address="192.168.33.100" rpc_address="192.168.33.100" 
192.168.33.101 cluster_name="Super Cluster" seeds="192.168.33.100,192.168.33.101,192.168.33.102" listen_address="192.168.33.101" rpc_address="192.168.33.101" 
192.168.33.102 cluster_name="Super Cluster" seeds="192.168.33.100,192.168.33.101,192.168.33.102" listen_address="192.168.33.102" rpc_address="192.168.33.102" 

A maioria das variáveis é opcional, exceto por **cluster_name** e **seeds**. A lista completa é:

	- cluster_name
	- seeds
	- listen_address
	- rpc_address
	- snitch

Lembre de trocar o username quando executar fora do Vagrant nos playbooks.

## AWS
	- Depende do Ansible do da biblioteca boto:
		$ sudo pip install ansible
		$ sudo pip install boto

	- Exportar as variáveis de ambiente com suas credenciais:
		$ export AWS_ACCESS_KEY_ID=<aws access key id>
		$ export AWS_SECRET_ACCESS_KEY=<aws secret access key>

	- configure o arquivo group_vars/all com os dados de sua conta:
		ssh_key_name: aws_devel
		aws_region: us-east-1
		ami_id: ami-9eaa1cf6
		instance_type: t2.micro
		vpc_id: vpc-ffffffff
		subnet_id: subnet-ffffffff
		vm_count: 3
		cidr_ip: 10.0.0.0/16

	$ ansible-playbook -i aws_hosts.ini cassandra_aws.yml --private-key ~/.ssh/aws_devel.pem
	- aws_devel.pem é a sua chave publica
	- aws_hosts.ini é um arquivo que contém apenas:
		[local]
		localhost

	- para removar o cluster vá ao painel do EC2 ou use $ ansible-playbook -i ./ec2.py remove_maquina.yml

## Vagrant
	- Certifique-se de que o Vagrant, Ansible e VirtualBox estejam instalados
	- Certifique-se de que o usuário no arquivo cassandra.yml (user:) seja vagrant
	- Inicie o cluster com $ vagrant up
	- Conecte nos nodes com $ vagrant ssh node0/node1/node2

## Direto em máquinas já criadas
	- Certifique-se de que o Ansible está instalado 
	- Certifique-se de que suas máquinas autenticam sem senha por ssh
	- Certifique-se de que o usuário no arquivo cassandra.yml (user:) seja ubuntu
	- Crie um arquivo de inventário seguindo o padrão de hosts_maquinas_virtuais.ini
	- Configure o parametro seeds com as máquinas do cluster
	- Execute $ ansible-playbook -i hosts.ini cassandra.yml

