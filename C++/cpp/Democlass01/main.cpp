#include <iostream>

using namespace std;

class votingclaculation{
public :
     void candidate()
     {
         int age ;
         cout << "Enter age:" << endl;
         cin >> age;
         string gender = "male";
        if(age>=18 && gender== "male")
         {
           cout << "He is Eligible for voting"  << endl;
         }
         else
         {
           cout << "She is Under processing for voting " << endl ;
         }
     }
};
int main()
{
    cout << "Election Details!" << endl;
    votingclaculation vc;
    vc.candidate();
    return 0;
}
