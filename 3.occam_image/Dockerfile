FROM svallero/htmframe:latest

MAINTAINER Sara Vallero <svallero@to.infn.it>

EXPOSE  5000
EXPOSE  5001
EXPOSE  22

USER    root
RUN     echo "root:your_password_goes_here" | chpasswd

# VOLUMES
VOLUME  ["/archive/home"]  

# Add GitLab known_hosts
RUN     ssh-keyscan gitlab.c3s.unito.it >> /root/.ssh/known_hosts

# For InfiniBand
RUN     set -ex \
        && yum -y install rdma libverbs opensm libmlx4 infiniband-diags ibutils \
        && yum clean all

RUN     systemctl enable rdma


WORKDIR /root/entrypoint/main/
ENTRYPOINT ["/sbin/tini", "/usr/bin/python", "/root/entrypoint/main/entrypoint.py"]

