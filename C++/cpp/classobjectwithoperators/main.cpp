#include <iostream>

using namespace std;

 class operatorexampleclass
{
 public :
     void addition()
     {
         int v1,v2,totalvalue;
         cout << "Enter V1" << endl << "Enter V2" << endl;
         cin >> v1 >> v2;
         cout << "Enter Total value:" << (v1+v2) << endl;
     }
      void subraction()
     {
         int v3,v4,totalvalue;
         cout << "Enter V3" << endl << "Enter V4" << endl;
         cin >> v3 >> v4;
         cout << "Enter Total value:" << (v3-v4) << endl;
     }
      void multiplication()
     {
         int v5,v6,totalvalue;
         cout << "Enter V5" << endl << "Enter V6" << endl;
         cin >> v5 >> v6;
         cout << "Enter Total value:" << (v5*v6) << endl;
     }
      void Division()
     {
         int v7,v8,totalvalue;
         cout << "Enter V7" << endl << "Enter V8" << endl ;
         cin >> v7 >> v8;
         cout << "Enter Total value:" << (v7/v8) << endl;
     }
void modulus()

};
void operatorexampleclass :: modulus()
{
int v9,v10,totalvalue;
cout << "Enter V9" << endl << "Enter V10" << endl ;
cin >> v9 >> v10;
cout << "Enter Total value:" << (v9%v10) << endl;
}


int main()
{
    cout << "Operators Example" << endl;

    operatorexampleclass oec;
    oec.addition();
    oec.subraction();
    oec.multiplication();
    oec.Division();
   oec . modulus();
    return 0;
}
