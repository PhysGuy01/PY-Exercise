#include <iostream>
#include <string>
using namespace std;

int main() {
    bool x = 0; // <-- con il dataType bool possiamo assegnare un valore booleano ad x (vero o falso) \
                        che è vero se gli associamo o "true" o 1, oppure falso se gli associamo "false" o 0
    bool y = 1; // stessa cosa per y

    // scritture equivalenti per entrambi sarebbero:\
            bool x = 0  <==>  bool x = false\
            bool y = 1  <==>  bool y = true

    if (x) cout << "Vero" << endl; else cout << "Falso" << endl;  // passo aggiuntivo: controlliamo se il valore di x è vero \
                                                                e allora outputtiamo "Vero" altrimenti "Falso"

    if (y) cout << "Vero" << endl; else cout << "Falso" << endl;  // stessa cosa per y

    return 0;
}