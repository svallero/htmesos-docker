EXECS=mpitest

MPICC?=/usr/mpi/gcc/openmpi-1.10.5a1/bin/mpicc

all: ${EXECS}

mpitest: mpitest.c
	${MPICC} -o mpitest mpitest.c

clean:
	rm ${EXECS}
