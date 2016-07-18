# This Dockerfile is modified from an example provided by Sven Dowideit from
# https://docs.docker.com/engine/examples/running_ssh_service/. It creates a
# container with an SSH daemon, and starts it as its CMD directive. This allows
# Ansible to provision it.

FROM ubuntu:{{ ubuntu_version }}

# Install the SSH server.
RUN apt-get update
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd

# Configure root login credentials to work with Vagrant.
RUN echo 'root:virtualmicromagnetics' | chpasswd
RUN sed -i 's|PermitRootLogin without-password|PermitRootLogin yes|' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's|session\s*required\s*pam_loginuid.so|session optional pam_loginuid.so|g' -i /etc/pam.d/sshd

# Start the daemon
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]