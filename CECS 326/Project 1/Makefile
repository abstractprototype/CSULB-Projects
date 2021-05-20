CC = gcc
CFLAGS = -pthread -o lab1exe

lab1:
	$(CC) $(CFLAGS) lab1version2.c 

lab1_sync:
	$(CC) $(CFLAGS) -DPTHREAD_SYNC lab1version2.c 

clean:
	rm lab1exe