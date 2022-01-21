#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void gift() {
	system("/bin/sh"); //launches a shell
}

void vuln() {
	char buf[24];

	void* addr_of_vuln = vuln;
	printf("Vuln is at %p. What's your name?\n", addr_of_vuln);
	gets(buf);
	printf("What do you want to write?\n");
	read(0, addr_of_vuln, 8);
	printf("See ya!");
}

int main() {
	setvbuf(stdin, NULL, 2, 0);
	setvbuf(stdout, NULL, 2, 0);
	setvbuf(stderr, NULL, 2, 0);
	vuln();
}
