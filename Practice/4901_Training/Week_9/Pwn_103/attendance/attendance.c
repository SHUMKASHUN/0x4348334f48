#include <stdio.h>

int w1, w2, w3;

void win1(){
	puts("haha!!\n");
	w1 = 1;
}

void win2(){
	puts("ok, calm down...\n");
	w2 = 2;
}

void win3(){
	puts("Alright...\n");
	w3 = 3;
}

void vuln(){
	char flag_buffer[64];
	puts("What are the magic words?\nanswer correctly, and ill give you the flag!\n");
	gets(flag_buffer);

	if(w1 == 1){
		char *filename = "flag";
		if(w2 == 2){
			char * mode = "r";
			if(w3 == 3){
				FILE *f = fopen(filename, mode);
				fgets(flag_buffer, 40, f);
				puts(flag_buffer);
			}
		}
	}
}

int main(){
	setvbuf(stdin,NULL,2,0);
	setvbuf(stdout,NULL,2,0);
	setvbuf(stderr,NULL,2,0);
	char space[256];
	vuln();
	return 0;
}