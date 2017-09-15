# Install a patched version of HTCondor from private repo.
# It is necessary to avoid a bug that prevents resources to be Uncalimed
# in the MPI case.

FROM    centos:7

MAINTAINER Sara Vallero <svallero@to.infn.it>

COPY    htcondor_patched /htcondor_patched
COPY    condor_local.repo /etc/yum.repos.d/condor_local.repo

RUN     set -ex \
        && yum -y install condor --enablerepo="condor_local" && yum clean all \
        && rm -rf /htcondor_patched /etc/yum.repos.d/condor_local.repo 

# general condor configuration file
COPY    condor_config /etc/condor/condor_config

# this below is generic for no MPI, and depends on the number of cores per container
COPY    condor_limit_slots /etc/condor/config.d/condor_limit_slots
