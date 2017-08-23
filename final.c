#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>
//#include <malloc.h>

void data_processing(const char *filename, const unsigned int im_height, const unsigned int im_width, const char *newfilename)
{
	FILE *file_in, *file_out;
	
	int i;
	unsigned int r,g,b;
	unsigned char x1,x2;

	//unsigned char len = strlen(filename);
	//char *newfilename = malloc(len-2);
	
	/*if (!newfilename)  handle error ;
    	memcpy(newfilename, filename, len-3);
    newfilename[len - 3] = 0;*/
    
    file_in = fopen(filename,"r+");
	if (file_in == NULL){
		printf("Error in opening input file!\n");
	}
	
	file_out = fopen(newfilename,"w+");
	if (file_out == NULL){
		printf("Error in opening output file!\n");
	}
	
	for(i=0; i <im_height*im_width ; i++)
	{
		fscanf(file_in,"%d",&r);
		fscanf(file_in,"%d",&g);
		fscanf(file_in,"%d",&b);
	
		x1=(r & 0xF8) | (g >> 5);
        x2=((g & 0x1C) << 3) | (b  >> 3);

		if(x1==10) x1++;
         fputc(x1,file_out);
       	if(x2==10) x2++;
         fputc(x2,file_out);
	}
	
	fclose(file_in);
	fclose(file_out);
	
	printf("Finished!\n");
}

