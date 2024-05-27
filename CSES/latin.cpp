#include <iostream>
#include <string>
using namespace std;
int main () {
    int qtd;
    string caracter;
    int A = 0, B = 0, C = 0, Iter = 0;
    int matriz[3][3];
    cin >>qtd;
    while (qtd--) {
        for (int i = 0; i < 3; i++) {
            cin >> caracter;
            for (int i = 0; i < caracter.length(); i++){
                if(caracter[i] == '?') {
                    Iter++;
                }
                else if(caracter[i] == 'A') {
                    A++;
                }
                else if(caracter[i] == 'B') {
                    B++;
                }
                else {
                    C++;
                }
            }
            if (Iter == 1) {
                if (A == 0) {
                    cout << "A\n";
                } 
                else if (B == 0) {
                    cout << "B\n";
                }
                else {
                    cout << "C\n";
                }
            }
        Iter = 0;
        A = 0;
        B = 0;
        C = 0;

        }
    }
    
    return 0;
}