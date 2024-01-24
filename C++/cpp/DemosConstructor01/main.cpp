#include <iostream>

using namespace std;
class student

{
public :

    student()
    {
    int Rollno;
    string std_Name  ;
    string section;

     cin >> Rollno >> std_Name >> section ;
     cout << Rollno << endl << std_Name << endl << section << endl;

    }
};
class Mark
{
public :
    int sub1;
    int sub2;
    int sub3;
    int totalmarks;

    void progresscard()
    {
      cout << "Enter the marks:" <<endl;
      cin >> sub1 ;
      cin >> sub2 ;
      cin >> sub3 ;
      totalmarks=(sub1+sub2+sub3);

      cout << totalmarks << endl  ;
    }
};


int main()
{
    cout << "student progress card Details!" << endl;
    student stds;
    Mark m;
    m. progresscard();
    return 0;
}
