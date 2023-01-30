#include<stdio.h>
#include<math.h>
#define SF 50
int main(){
    float x,y;
    int i,k;
    clrscr();
    for(x = -3;x<=3;x=x+0.25)
    {
        y=exp(-x*x/2);
        k=SF*y;
        printf("\n |");
        for ( i = 0; i < k; i++)
        {
            printf(" ");
        printf("*");
        }
        
    }
    return 0;

}