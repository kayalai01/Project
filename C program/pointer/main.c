#include <stdio.h>
#include <stdlib.h>

int main()
{   int a= 13, b= 98;
    printf("Enter  A value : %d\t\n",a);
    printf("Address of   A value : %d\t\n",&a);
    printf ("-----------\n\n");
    printf("Enter  A value : %d\t\n",b);
    printf("Address of  A value : %d\t\n",&b);
    printf ("-----------\n\n");

    int *p=&a;
    printf("Enter value of p :%d \t\n",p);
    printf("Address value of P:%d \t\n",&p);
    printf("Stored values p Addressed to the Addressed a: %d\t\n",*p);
    printf("---------------\t\n");

    int **q=&p;
    printf ("Enter value of q : %d \t\n",q);
    printf ("Address value of q: %d \t\n",&q);
    printf ("Stored values of q into the p Addressed value : %d \t\n ",**q);
    printf ("------------\n\t");


    int ***r=&q;
    printf ("Enter value of r: %d \t\n",r);
    printf ("Enter value of r : %d \t\n",r);
    printf ("Address value of r: %d \t\n",&r);
    printf ("Stored values of r into the q Addressed value : %d \t\n ",***r);
    printf ("------------\n\t");

    return 0;
}
