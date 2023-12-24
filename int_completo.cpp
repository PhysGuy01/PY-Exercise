#include <iostream>
#include <string>
#include <math.h>
#define pi 3.1415926535897932384626433832
using namespace std;

double gauss(double x, double &sigma, double &mu){
    return 1/(sigma * sqrt(2*pi)) * exp(-pow(x - mu, 2)/(2 * pow(sigma, 2)));
}

double integral(double a, int n, double &sigma, double &mu) {

    double d = (mu - a) / n;
    double integrale = 0;
    for (int i = 0; i < n; i++) 
        integrale += (gauss(a + i * d, sigma, mu) + gauss(a + (i + 1) * d, sigma, mu))/2;
    
    return d * integrale;
}

int main(){
    double x, mu, sigma;
    
    cout << "\nCalcolo dell'integrale da una variabile standardizzata.\nInserire mu, sigma e x (eg. 0 1 -1.4): ";
    cin >> mu >> sigma >> x;

    while(cin.fail() || x == mu) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(),'\n');
        cout << "Valore errato, inserisci tre numeri: ";
        cin >> mu >> sigma >> x;
    }   

    double z = abs(integral(x, 10000, sigma, mu));

    if (x < mu) 
        cout << "Integrale compreso tra " << x << " e " << mu << "(%): " << z * 100 << endl;
    else 
        cout << "Integrale compreso tra " << mu << " e " << x << "(%): " << z * 100 << endl;


    cout << "Integrale coda "; 
    if (x > mu) cout << "destra: "; else cout << "sinistra: ";
    cout << 50 - z * 100 << endl;

    if (x < mu) 
        cout << "Integrale tra " << x << " e " << mu + abs(x - mu) << ": " << 200 * z << endl; 
    else 
        cout << "Integrale tra " << mu - abs(x - mu) << " e " << x << ": " << 200 * z << endl;

    cout << "Integrale di entrambe le code: " << 100 - (z * 200) << endl << endl;

    return 0;
}