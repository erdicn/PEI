/******************************************************
*************Chi-square fitting**************
Exponential Fitting: y=Ae^bx
******************************************************/
#include<stdio.h>
#include<math.h>
/*****
Function that calculates and returns the slope of the best fit line
Parameters:
N: no. of data-points
x[N]: array containing the x-axis points
y[N]: array containing the corresponding y-axis points
*****/
double slope(int N, double x[N], double y[N]){
    double m;
    int i;
    double sumXY=0;
    double sumX=0;
    double sumX2=0;
    double sumY=0;
    for(i=0;i<N;i++){
        sumXY=sumXY+x[i]*y[i];
        sumX=sumX+x[i];
        sumY=sumY+y[i];
        sumX2=sumX2+x[i]*x[i];
    }
    sumXY=sumXY/N;
    sumX=sumX/N;
    sumY=sumY/N;
    sumX2=sumX2/N;
    m=(sumXY-sumX*sumY)/(sumX2-sumX*sumX);
    return m;
}
/*****
Function that calculates and returns the intercept of the best fit line
Parameters:
N: no. of data-points
x[N]: array containing the x-axis points
y[N]: array containing the corresponding y-axis points
*****/
double intercept(int N, double x[N], double y[N]){
    double c;
    int i;
    double sumXY=0;
    double sumX=0;
    double sumX2=0;
    double sumY=0;
    for(i=0;i<N;i++){
        sumXY=sumXY+x[i]*y[i];
        sumX=sumX+x[i];
        sumY=sumY+y[i];
        sumX2=sumX2+x[i]*x[i];
    }
    sumXY=sumXY/N;
    sumX=sumX/N;
    sumY=sumY/N;
    sumX2=sumX2/N;
    c=(sumX2*sumY-sumXY*sumX)/(sumX2-sumX*sumX);
    return c;
}
int main(){
    int N;
    printf("Enter the no. of data-points:\n");
    scanf("%d",&N);
    double x[N], y[N], Y[N];
    printf("Enter the x-axis values:\n");
    int i;
    for(i=0;i<N;i++){
        scanf("%lf",&x[i]);
    }
    printf("Enter the y-axis values:\n");
    for(i=0;i<N;i++){
        scanf("%lf",&y[i]);
    }
    for(i=0;i<N;i++){
        Y[i]=log(y[i]);
    }
    printf("The exponential fit is given by the equation:\n");
    double m=slope(N,x,Y);
    double c=intercept(N,x,Y);
    double A, b; //y=Ae^bx
    A=exp(c);
    b=m;
    printf("y = %lf e^(%lf)x",A,b);
    return 0;
}