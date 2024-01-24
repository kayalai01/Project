#include <iostream>

using namespace std;

class National

 {
 private :
    string country= "INDIA";
    int rank_status=1;

 public :
     string categories = "Sports categories" ;
     string sports = "javelin throw";

     void medalist()
     {
         string name ="Neeraj Chopra";
         int age = 27;
         int height = 18;
         cout << "Enter Name :" << name << endl << "Current Age:" << age << endl << "Height: " << height ;

     }
     void print ()
     {
         string abt= "country";
         int status = rank_status;
     }
 };

class world : public National

{
public :

    void statement ()
    {
        cout << "INDIA GOLD MEDALIST IN 2024" << endl;
    }
};






int main()
{ National N;
 world W;
 W.statement();
 N.medalist();
 W.medalist();
 int status;
 N.print();
    return 0;
}
