#include <iostream>

using namespace std;

int main()
{  /*string candidate;
    cout << "Enter string  value " << endl;
    cin >> candidate;
    cout << "Enter candidate Name:" << candidate << endl;
    fflush (stdin);
    cout << "Enter string  value " << endl;
    getline (cin , candidate);
    cout << "Enter candidate Name:" << candidate << endl;*/


    /*  string candidate;
    cout << "Enter string  value " << endl;
    getline (cin , candidate);
    cout << "Enter candidate Name:" << candidate << endl;

  fflush (stdin);
    cout << "Enter string  value " << endl;
    getline (cin , candidate);
    cout << "Enter candidate Name:" << candidate << endl;*/

    string firstname;
    string lastname;
    cout << "Enter firstname: "<< endl;
    cin >>  firstname;
    cout << "Enter lastname: "<< endl;
    cin >>  lastname;
    cout << firstname +" "+ lastname;
    //string fullname = firstname . append (lastname);
    firstname.push_back ('M');
    cout << firstname;



    return 0;
}
