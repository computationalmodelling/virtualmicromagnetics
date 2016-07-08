# This makefile is the user interface to jobs that the user may wish to carry
# out using virtual machines.

## Container targets
full-container:
	ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars="type=container container_name=virtualmicromagnetics/full playbook=provision_virtualmicromagnetics_full_container.yml hookbook=hook_container.yml extra_resources_dir=guest_resources/"

lite-container:
	ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars="type=container container_name=virtualmicromagnetics/lite playbook=provision_virtualmicromagnetics_lite_container.yml hookbook=hook_container.yml extra_resources_dir=guest_resources/"

oommf-container:
	ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars="type=container container_name=virtualmicromagnetics/oommf playbook=provision_virtualmicromagnetics_oommf_container.yml hookbook=hook_container.yml extra_resources_dir=guest_resources/"

magpar-container:
	ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars="type=container container_name=virtualmicromagnetics/magpar playbook=provision_virtualmicromagnetics_magpar_container.yml hookbook=hook_container.yml extra_resources_dir=guest_resources/"

nmag-container:
	ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars="type=container container_name=virtualmicromagnetics/nmag playbook=provision_virtualmicromagnetics_nmag_container.yml hookbook=hook_container.yml extra_resources_dir=guest_resources/"

fidimag-container:
	ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars="type=container container_name=virtualmicromagnetics/fidimag playbook=provision_virtualmicromagnetics_fidimag_container.yml hookbook=hook_container.yml extra_resources_dir=guest_resources/"

## VM targets
full-vm: full
lite-vm: lite
oommf-vm: oommf
magpar-vm: magpar
nmag-vm: nmag
fidimag-vm: fidimag

# This target builds a virtual hard disk file containing various open
# micromagnetics simulation technologies and other convenient packages.
full:
	ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars="type=vm vm_name=virtualmicromagnetics-full playbook=provision_virtualmicromagnetics_full_vm.yml hookbook=hook_vm.yml extra_resources_dir=guest_resources/"

# This target builds a virtual hard disk file containing various open
# micromagnetics simulation technologies.
lite:
	ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars="type=vm vm_name=virtualmicromagnetics-lite playbook=provision_virtualmicromagnetics_lite_vm.yml hookbook=hook_vm.yml extra_resources_dir=guest_resources/"

# This target builds a virtual hard disk file containing an OOMMF
# installation.
oommf:
	ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars="type=vm vm_name=virtualmicromagnetics-oommf playbook=provision_virtualmicromagnetics_oommf_vm.yml hookbook=hook_vm.yml extra_resources_dir=guest_resources/"

# This target builds a virtual hard disk file containing a Magpar
# installation.
magpar:
	ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars="type=vm vm_name=virtualmicromagnetics-magpar playbook=provision_virtualmicromagnetics_magpar_vm.yml hookbook=hook_vm.yml extra_resources_dir=guest_resources/"

# This target builds a virtual hard disk file containing a Nmag
# installation.
nmag:
	ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars="type=vm vm_name=virtualmicromagnetics-nmag playbook=provision_virtualmicromagnetics_nmag_vm.yml hookbook=hook_vm.yml extra_resources_dir=guest_resources/"

# This target builds a virtual hard disk file containing a fidimag
# installation.
fidimag:
	ansible-playbook master.yml -c local -i localhost, -v -k --extra-vars="type=vm vm_name=virtualmicromagnetics-fidimag playbook=provision_virtualmicromagnetics_fidimag_vm.yml hookbook=hook_vm.yml extra_resources_dir=guest_resources/"
