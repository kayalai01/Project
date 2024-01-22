#include <stdio.h>
#include <stdlib.h>

int main()

{
    int a=6;
    int b=3;
     addition(a,b);
     subraction (a,b);
      multipication(a,b);
      Division(a,b);
      assignment(a,b);
      increment(a);
      decrement(b);
      comparision(a,b);
      Logicals(a,b);
      ifstatement (a,b);
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
int multipication (int a, int b)
{
     int c;
    c=a*b;
    printf("multiply is :%d\n\n",c);
    return 0;

}
int Division (a,b)
{
    int D;
    D=a/b;
    printf("Division is :%d\n\n",D);
    return 0;
}

int assignment(int a, int b)

{
    printf("_______Assignment________ \n\n");
    a=b;
    printf("P value is :%d\n\n",a=b);
    a+=b;
    printf("Q value is :%d\n\n",a+=b);
    a-=b;
    printf("R value is :%d\n\n",a-=b);
    a/=b;
    printf("S value is :%d\n\n",a/=b);
    a%=b;
    printf("T value is :%d\n\n",a%=b);
    a&=b;
    printf("U values is:%d\n\n",a&=b);
     a&=6;
    printf("U1 values is:%d\n\n",a&=6);
    return 0;
}

int increment(int a)
{

    printf("_______Increment and  Decrement________ \n\n");
    printf("increment is:%d\n\n",a);
     ++a;
    return 0;
}
int decrement(int b)
{


    printf("decrement is:%d\n\n",b);
     --b;
    return 0;
}
int comparision(int a, int b)
{
    printf("_______Comparisiom________ \n\n");

    a==b;
    printf("X value is :%d\n\n",a==b);

    a==6;
    printf("X1 value is :%d\n\n",a==6);

    a>b;
    printf("Y value is :%d\n\n",a>b);

    a<b;
    printf("Y1 value is :%d\n\n",a<b);

    a>=b;
    printf("Z value is :%d\n\n",a>=b);

    a<b;
    printf("Z1 value is :%d\n\n",a<=b);
    return 0;
}
int Logicals (int a, int b)
{
    printf("_______Logicals and IF clause________ \n\n");

  if (a>0 && b<10)
 {
 printf("you are Eligible to vote\n\n");

 if (a>20 || b<10)
 printf("you are Not Eligible to vote\n\n");

 if (!a<5 && b<5);
 printf("its correct value \n\n");
  }
  return 0;
}
int ifstatement (int a, int b)
{


 printf("_______ IF and Else programm ________ \n\n");
 if (a=4) && (a<2);
 {
 printf("least the point%d\n\n",a);

 }
 else
 (
  printf("instant the point%d\n\n",a);

  )
return 0;
)
