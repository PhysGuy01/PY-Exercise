#include <iostream>
#include <gmpxx.h>
using namespace std;

void P(const mpf_t n; const int numBits; const mpf_t p;) {
    mpf_set_default_prec(numBits);
    p = 1;
    for (mpf_ j = 0; j <= n; j++) {
        mpf_mul(p, p, j)
        p *= -(6*j - 1)*(2*j - 1)*(6*j - 5);
    }
}

void Q(const mpf_t n; const int numBits; const mpf_t p;) {
    mpf_set_default_prec(numBits);
    p = 1;
    for (int j = 0; j <= n; j++) {
        p *= -(6*j - 1)*(2*j - 1)*(6*j - 5);
    }
}

int main() {
    mpf_t n, p;
    mpf_init(n);
    mpf_init(p);

    cout << "Enter the number of digits you'd like to calculate: ";
    gmp_scanf("%Ff", n);

    int numBits = (int)ceil(n * log2(10));



    mpf_clear(n);
    mpf_clear(p);
    //remember to free the memory!!
    return 0;
}