#include <iostream>
#include <math.h>
#include <string>
using namespace std;

// c++ non può lavorare con grossi decimali come python quindi
// voglio creare un algoritmo che ad ogni iterazione calcoli l'iesima cifra del pi greco
// fino all'n-esima e la inserisca in una stringa.... più facile a dirsi che a farsi 
// gli algoritmi principali da usare per calcolare l'n-esima cifra del pi greco
// sono principalmente basati sulla formula BBP ma non capisco come funzionano...

//  look into: https://www.experimentalmath.info/bbp-codes/
// https://mathworld.wolfram.com/Digit-ExtractionAlgorithm.html
    
int main() {

    // dn = int(10*frac(10^(n-1) * 1))
    // algoritmo per n-esima cifra del pi greco
    // dn = floor(10 * (10^(n-1)-floor(10^(n-1) * k)))
    cout << "n digits of pi: ";
    int n;
    cin >> n;
    string pi = "3.141";
    int k = 1;
    float dn;

    //non funziona un cazzo lol
    for(int i = 0; i <= n; i++){
        dn = floor(10 * (pow(10,(k))-floor(10^(k) * k)));
        cout << dn << endl;
        pi.append(to_string( (int)dn ));
        k = dn;
    }
    cout << pi;
    return 0;
}