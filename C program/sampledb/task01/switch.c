#include <stdio.h>
int main()
{
    int a;
    int b;
    int c;
    char d;
    int e;
     printf("Enter the value :\n\n");
    scanf("%d",&a);
    if(a==2)
    {
    printf("Enter the 1St value:\n\n");
    scanf("%d",&b);
    printf("Enter the 2nd value:\n\n");
    scanf("%d",&c);
    printf("Enter operator:\n"); 
    scanf (" %c",&d);
    switch(d)
    {
    case'+':
      printf("The added value :%d\n\t",b+c);
      break;

      case'-':
      printf("The Sub value :%d\n\t",b-c);
      break;
    }
    }
    else
    {
   printf("Enter the 1St value:\n\n");
    scanf("%d",&b);
    printf("Enter the 2nd value:\n\n");
    scanf("%d",&c);
    printf("Enter operator:\n"); 
    scanf ("%d",&d);
    switch(d)
    {
    case 1:
      printf("The added value :%d\n\t",b*c);
      break;
     case 2:
      printf("The Sub value :%d\n\t",b/c);
      break;  
    }
    }
    return 0;
}
