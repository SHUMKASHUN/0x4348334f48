#include <stdio.h>

void convo() {
	char buf[16];
	printf("Mr. RBP says he feels like %p today. Want me to send him a message for you?\n", (buf + 16));
	gets(buf);
	printf("Hope he responds soon!");
}

int main() {
	setvbuf(stdin,NULL,2,0);  // just
	setvbuf(stdout,NULL,2,0); // for
	setvbuf(stderr,NULL,2,0); // setup
	convo();
}
