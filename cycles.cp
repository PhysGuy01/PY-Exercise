// same code code but in c++
#include <iostream>
#include <fstream>
using namespace std;

int main(){
    clock_t begin = clock();
    fstream data;
    data.open("data.dat", ios::in);
    float sum=0.0, i=0, n=0;

    while(1) {
        data >> n;
        if (data.eof()) break;
        sum += n;
        i++;
    }
    float avg = sum / i;
    cout << "\ncpp:\n\nmedia: " << avg << endl;

    clock_t end = clock();
    double time_spent = (double)(end - begin) / CLOCKS_PER_SEC;
    cout <<"--- " << time_spent << " seconds ---" << endl;

    return 0;
} 

//  cout << sum << endl;
//  cout << i << endl;
