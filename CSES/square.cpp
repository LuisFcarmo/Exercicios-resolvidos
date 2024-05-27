#include <iostream>
#include <math.h>
using namespace std;
int main () {
    int qtd;
    int qtd2;
    int valor;
    double total = 0;
    double resultado = 0;

    cin >> qtd;
    
    while (qtd--)
    {
        cin >> qtd2;
        while (qtd2--)
        {
            cin >> valor;
            total += valor;
        }
        resultado = sqrt(total);
       ;
        if(resultado - (int) resultado != 0) {
            cout << "NO\n";
        } else {
            cout << "YES\n";
        }
        total = 0;
    }
    


    return 0;
}