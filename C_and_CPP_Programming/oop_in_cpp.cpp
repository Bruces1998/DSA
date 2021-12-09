#include <iostream>

using namespace std;

class person
{
    char name[20];
    public:
    int id;
    void getDetails(){}
};

int main()
{
    person p1;
    p1.id = 1;
    cout << p1.id;

}