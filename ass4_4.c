#include <stdio.h> 
#include <stdlib.h> 
#include<math.h>
#include<time.h>

int main()
{
	double x,y;
	long int N=10;
	FILE *data;
	data=fopen("random.txt","w");

	srand(time(0));
	

	for(long int i=0; i<N; i++)
	{
		x=rand()/(double)RAND_MAX;
		y=-0.5*log(x);
		fprintf(data,"%lf\n",y);
	}
	fclose(data);
	//system("plot.py"); //to plot the histogram I've used python



return 0;
}