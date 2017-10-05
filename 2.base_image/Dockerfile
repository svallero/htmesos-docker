### Base image for INDIGODC HTMESOS framework 

FROM    svallero/htcondor-patched

MAINTAINER Sara Vallero <svallero@to.infn.it>

### PORTS
# 5000 if for Mesos/Marathon health-checks
EXPOSE  5000
# 5001 exposes HTCondor metrics for auto-scaling
EXPOSE  5001
# 22 is for ssh
EXPOSE  22

USER    root
RUN     echo "root:your_password_goes_here" | chpasswd

### Tini (init for containers)
ENV     TINI_VERSION v0.9.0
ADD     https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /sbin/tini
RUN     chmod +x /sbin/tini

### Supervisord (process control system)
RUN     yum makecache fast
RUN     set -ex \
        && yum -y install epel-release \
        && yum -y install git vim wget procps curl python-pip && yum clean all\
        && pip install supervisor supervisor-stdout 
# this is the minimal configuration file,
# the sssd configuration is added at runtime if LDAP is enabled
COPY    config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf 
 
### Ssh server 
# users should be able to login on the Submitter 
RUN     set -ex \ 
        && yum -y install bind-utils openssh-clients openssh-server && yum clean all \ 
        && mkdir -p /root/.ssh && chmod 700 /root/.ssh \ 
        && mkdir -p /var/log/ssh/ && mkdir /var/run/sshd 
# here in particular note the "AuthorizedKeysCommand" section
# needed for LDAP
COPY    config/sshd_config /etc/ssh/sshd_config 

### Health-checks
COPY    repos/condor_official.repo /etc/yum.repos.d/condor_official.repo 
RUN     set -ex \ 
        &&  yum install -y condor-python-8.4.8-1.el7.x86_64 --showduplicates --enablerepo=htcondor-stable \
        && yum clean all

RUN     set -ex \ 
        && mkdir -p /opt/health/master/ /opt/health/executor/ /opt/health/submitter/ \ 
        && pip install Flask requests         

COPY    healthchecks/master_healthcheck.py /opt/health/master/healthcheck.py 
COPY    healthchecks/submitter_healthcheck.py /opt/health/submitter/healthcheck.py 
COPY    healthchecks/executor_healthcheck.py /opt/health/executor/healthcheck.py 
# only needed if you use the HTMesos framework
COPY    healthchecks/executor_healthcheck_htmf.py /opt/health/executor/healthcheck_htmf.py 

### Publish condor queue status for elasticity
# only needed if you use the HTMesos framework
RUN     set -ex \ 
        && mkdir -p /opt/condor_status/ \ 
        && yum -y remove python-pip          
COPY    condor_status/publish_status.py /opt/condor_status/publish_status.py

### Patch to avoid mpirun timeout looking for IB device
# should be fixed in Centos 7.4
RUN     wget https://kojipkgs.fedoraproject.org//packages/libfabric/1.4.0/2.fc26/x86_64/libfabric-1.4.0-2.fc26.x86_64.rpm && yum -y localinstall libfabric-1.4.0-2.fc26.x86_64.rpm 

### This part is for LDAP
RUN     set -ex \ 
        && yum install -y openldap-clients sssd libnss-sss libpam-sss ca-certificates\
        && yum clean all 
# the name of your LDAP server is configured at runtime
COPY    scripts/ldapAuthorizedKeysCommand /sbin/ldapAuthorizedKeysCommand
RUN mkdir -p /var/run/sshd

# sssd daemon config
COPY config/sssd.conf /etc/sssd/sssd.conf
RUN  chmod 600 /etc/sssd/sssd.conf
COPY config/nsswitch.conf /etc/nsswitch.conf 

### For X forwarding
RUN     set -ex \
        && yum -y install xorg-x11-xauth.x86_64 \ 
        && yum clean all

# VOLUMES
# this is only for OCCAM, should be moved away
VOLUME  ["/archive/home"]

### ENTRYPOINT
COPY    entrypoint /root/entrypoint 
WORKDIR /root/entrypoint/main/
ENTRYPOINT ["/sbin/tini", "/usr/bin/python", "/root/entrypoint/main/entrypoint.py"] 
