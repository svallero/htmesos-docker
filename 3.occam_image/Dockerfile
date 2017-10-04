#FROM svallero/htmframe:latest
FROM centos:latest

MAINTAINER Sara Vallero <svallero@to.infn.it>

#EXPOSE  5000
#EXPOSE  5001
#EXPOSE  22

#USER    root
#RUN     echo "root:your_password_goes_here" | chpasswd

# VOLUMES
#VOLUME  ["/archive/home"]  

# Add GitLab known_hosts
#RUN     ssh-keyscan gitlab.c3s.unito.it >> /root/.ssh/known_hosts

# For InfiniBand
#RUN     set -ex \
#        && yum -y install rdma libverbs opensm libmlx4 infiniband-diags ibutils \
#        && yum clean all

#RUN     systemctl enable rdma

# MPI MELLANOX PATCHED
COPY    MLNX_OFED_LINUX-3.4-2.0.0.0-3.10.0-514.2.2.el7.x86_64 /root/MPI_MELLANOX
#COPY    modules/3.10.0-514.2.2.el7.x86_64/modules.* /lib/modules/3.10.0-514.2.2.el7.x86_64/
RUN     set -ex \
        && yum -y install libnl lsof numactl-libs numactl-devel ethtool gcc-gfortran tcsh \
        && yum -y install make gtk2 atk cairo tcl tk perl\
        && yum clean all

# We assume that the RPMs are already produced
WORKDIR /root/MPI_MELLANOX/MLNX_OFED_LINUX-3.4-2.0.0.0-rhel7.3-ext
#COPY    ofed_occam.conf ofed_occam.conf
RUN     set -ex \
        && ./mlnxofedinstall --force --without-fw-update --user-space-only -q 

# Enable the local yum repo
#COPY    mlx_ofed.repo /etc/yum.repos.d/mlx_ofed.repo 
#WORKDIR /root/MPI_MELLANOX/MLNX_OFED_LINUX-3.4-2.0.0.0-rhel7.3-ext/RPMS
#RUN     yum localinstall -y openmpi-1.10.5a1-1.34100.x86_64.rpm 

# Install some useful stuff
#RUN     set -ex \
#        && yum -y install make gcc numactl-libs\
#        && yum clean all
#VOLUME ["/usr/mpi/gcc/openmpi-1.10.5a1/"] 
# one could also expose the volume at runtime
#COPY   openmpi-1.10.5a1/ /usr/mpi/gcc/openmpi-1.10.5a1/ 

#RUN    useradd -d /archive/home/svallero svallero
#COPY   mpitest /archive/home/svallero/mpitest
#RUN    chown svallero:svallero /archive/home/svallero/mpitest

#ENV    PATH="/usr/mpi/gcc/openmpi-1.10.5a1/bin:${PATH}"

#WORKDIR /root/entrypoint/main/
#ENTRYPOINT ["/sbin/tini", "/usr/bin/python", "/root/entrypoint/main/entrypoint.py"]
#USER    svallero
#ENV     PATH="/usr/mpi/gcc/openmpi-1.10.5a1/bin:${PATH}"
#WORKDIR /archive/home/svallero/mpitest
#ENTRYPOINT ["mpirun", "-np", "4", "-mca", "btl", "self,openib", "mpitest"]
#ENTRYPOINT ["/bin/ls", "/dev"]


