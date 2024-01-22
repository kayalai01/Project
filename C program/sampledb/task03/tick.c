#include <stdio.h>
int main()
{
    int a;
    int b;
    int c;
    int d;
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
    scanf ("%c",&operator);
    switcth(operator);
    
    {
    case1:
      printf("The added value :%d\n\t",b+c);
      break;

      case2:
      printf("The Sub value :%d\n\t",b-c);

      break;

    }
    else
    {

      printf("Enter the 1St value:\n\n");
    scanf("%d",&b);
    printf("Enter the 2nd value:\n\n");
    scanf("%d",&c);
    printf("Enter operator:\n"); 
    scanf ("%c",&operator);
    switcth(operator);
    
    {
    case1:
      printf("The added value :%d\n\t",b+c);
      break;

      case2:
      printf("The Sub value :%d\n\t",b-c);

      break;



       
    }
    return 0;
}
