#include<stdio.h>

void bare(){
	char name[16];
	puts("What is your name?");
	gets(name);
}

int main(){
	setvbuf(stdin,NULL,2,0);
	setvbuf(stdout,NULL,2,0);
	setvbuf(stderr,NULL,2,0);
	bare();
	return 0;
}

