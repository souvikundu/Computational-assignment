#include <stdio.h> 
#include <stdlib.h> 
#include<math.h>
#include<time.h>

int main()
{
	double x,y;
	long int N=10000;
	FILE *data;
	data=fopen("random.txt","w");

	srand(time(0));
	

	for(long int i=0; i<N; i++)
	{
		x=(double)rand()/(double)RAND_MAX;
		y=-0.5*log(x);
		fprintf(data,"%lf\n",y);
	}
	fclose(data);
	system("python3 plot.py"); //to plot the histogram I've used python



return 0;
}