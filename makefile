CC = g++

all: int_completo

int_completo: int_completo.cpp
	$(CC) -o $@ $<