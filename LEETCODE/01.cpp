#include <iostream>
#include <string>
using namespace std;
int main()
{
    string x;
    int p;

    cin >> p;
    cin >> x;
    int qtda = 0;
    int qtdfinal = 0;

    for (int i = 0; i < x.length(); i++)
    {
        if (x[i] == 'a')
        {
            qtda++;
            if (qtda == 2)
            {
                qtdfinal++;
            }
            if (qtda >= 2)
            {
                qtdfinal++;
            }
        }
        else
        {
            qtda = 0;
        }
    }
    cout << qtdfinal;

    return 0;
}