#include <iostream>
using namespace std;
class myfirstclass

{
public :
int a=0;

void multiply()
{
int x,y;
cin >>x>>y;
cout <<(x*y);
}
};
int addition()
{
    int a,b,c;
    cin >> a >> b;
    c=a+b;
    cout<<c;
    return 0;
}
void myfirstclass :: msgsecond()
{
    cout<< "welcome to class and object";

}
int main ()
{
addition();
myfirstclass mfc;
    cout << mfc.a;
  mfc.multiply();

    return 0;
}




















