#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void file_gen(char *str, int len)
{
int i;
FILE *fp;

fp = fopen(str,"w");
//Generate numbers
for (i = 0; i < len; i++)
{
fprintf(fp,"%lf\n",5*(double)rand()/RAND_MAX);
}
for (i = 0; i < len; i++)
{
fprintf(fp,"%lf\n",(-5)*(double)rand()/RAND_MAX);
}
fclose(fp);
}

int  main(void)
{
file_gen("p.dat",5);
return 0;
}
