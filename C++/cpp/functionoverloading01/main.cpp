#include <iostream>
using namespace  std;

class AIBATCH

{ public:
    void FirstBatch()
    {
        int slno;
        string Name;
        int YOP;
        string qualification;

       cout << "slno" << endl << "Enter Name:" << endl << "year of passing" << endl << "qualification" << endl;
       cin >> slno >> Name >> YOP >> qualification;

    }
   void FirstBatch(string msg)
   {
       cout<< "enter the msg :" << msg << endl;
   }
};

int main ()
{
   AIBATCH  AI, AI1;

   AI . FirstBatch();
   string msg;
   AI1 . FirstBatch("Hii");
   return 0;
}
