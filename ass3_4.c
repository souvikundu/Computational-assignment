#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<fftw3.h>
#define xmax 50.0
#define xmin -50.0
#define N 256
#define RE 0
#define IM 1


void set_data (fftw_complex* raw_data,double resolution)
{
  int i;
  double x;
  for (i=0;i<N;i++)
  {
    x=xmin+i*resolution;			/* Generating the raw data of the given sinc function*/
    if(x!=0)
    {
        raw_data[i][RE]=exp(-pow(x,2));
    }
    else
        raw_data[i][RE]=1; 
    raw_data[i][IM]=0;
  }
}

int main()
{
	FILE *star;
    	star=fopen("raw4.txt","w");		/*opening  a file in a write mode*/
	fftw_complex *raw_data;
	fftw_complex *final;		/*starting arrays to store initial and final data*/
	double frequency;
	double resolution=(xmax-xmin)/(N-1);
	double AFT_real,AFT_imag;

	raw_data  = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);    /*allocating memory*/
	final  = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
	
  	fftw_plan p;    /*DEfinition of FFTW */
	
	p = fftw_plan_dft_1d(N, raw_data, final, FFTW_FORWARD, FFTW_ESTIMATE);

	set_data(raw_data,resolution);

  	fftw_execute(p); 		/*creates the discrete fourier transform */

	int i;
	for (i=0;i<N;i++)
  	{
	   if (i<=N/2-1)
	   {
		frequency=(2*M_PI/(N*resolution))*(i);
	   }
	   else
	   {
		frequency=(2*M_PI/(N*resolution))*(i-N);
	   }
	   AFT_real=(1/sqrt(N))*final[i][RE];   /* normalisation of the fourier transform*/
   	   AFT_imag=(1/sqrt(N))*final[i][IM];
	   AFT_real= resolution*sqrt(N/(2*M_PI))*(cos(frequency*xmin)*AFT_real+sin(frequency*xmin)*AFT_imag);
	   AFT_imag= resolution*sqrt(N/(2*M_PI))*(cos(frequency*xmin)*AFT_imag-sin(frequency*xmin)*AFT_real);
	   fprintf(star,"%e\t%e\n",frequency,AFT_real);
	  
 	}
	
	fftw_destroy_plan(p);
	fftw_free(raw_data); 
	fftw_free(final);
	return (0);
}