#include <iostream>
#include <string>
#include <math.h>
#define pi 3.14159265358979323846
using namespace std;

double gauss(double x, double &sigma, double &mu){
    return 1/(sigma * sqrt(2*pi)) * exp(-pow(x - mu, 2)/(2 * pow(sigma, 2)));
}

double integrate_gaussian(double a, double b, int n, double &sigma, double&mu) {
    double d = (b-a)/n;
    double integrale = 0;
    for (int i = 0; i < n; i++) 
        integrale += (gauss(a + i * d, sigma, mu) + gauss(a + (i + 1) * d, sigma, mu))/2;
    
    return d*integrale;
}

int main(){
    double mu, sigma, n, a, b;
    cout << "Inserire il valor medio: ";
    cin >> mu;

    cout << "Inserire la dev standard: ";
    cin >> sigma;

    cout << "Inserire a: ";
    cin >> a;

    cout << "Inserire b: ";
    cin >> b;

    cout << "Inserire il numero di steps per la precisione: ";
    cin >> n;

    double integral = integrate_gaussian(a,b,n,sigma,mu);
    cout << "\nIntegrale della Gaussiana tra " << a << " e " << b << " e': " << integral << endl;
    cout << "Probabilita' sottesa: " << integral * 100 << endl;
    cout << "Probabilita' delle code: " << 100 - (integral * 100) << endl;
 
    return 0;
}