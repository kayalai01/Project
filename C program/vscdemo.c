#include <stdio.h>


int main()

{
    int a=6;
    int b=3;
    int addition(a,b);
     int subraction (a,b);
      
     return 0;
}
int addition(int a, int b)
{
    printf("\n\n_______Arthimatic________ \n\n");
    int c;
    c=a+b;
    printf("sum is :%d\n\n",c);
    return 0;
}
int subraction (int a, int b)
{

    int c;
    c=a-b;
    printf("sub is :%d\n\n",c);
    return 0;

}

