#include <stdio.h>

void one_link_only(){
	char buf[16];
	puts("Ill only let you have one link!");
	read(0,buf,32);
}

int main(){
	char buf[64];
	setvbuf(stdin,NULL,2,0);
	setvbuf(stdout,NULL,2,0);
	setvbuf(stderr,NULL,2,0);
	puts("good luck...");
	read(0,buf,64);
	one_link_only();
	return 0;
}