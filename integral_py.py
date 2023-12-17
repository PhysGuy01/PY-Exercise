from math import sqrt, exp, pow

pi = 3.141592653589793238462643

def gauss(x, mu, sigma):
    return 1/(sigma * sqrt(2 * pi)) * exp(-pow(x - mu, 2)/(2 * pow(sigma, 2)))

def integrale(a, b, n, sigma, mu):
    d = (b - a)/n
    integrale = 0
    for i in range(n):
        integrale += (gauss(a + i * d, mu, sigma) + gauss(a + (i + 1) * d, mu, sigma))/2
    
    return d * integrale


mu = float(input("\nInserire mu: "))
sigma = float(input("Inserire dev standard: "))
a = float(input("Inserire a: "))
b = float(input("Inserire b: "))
n = int(input("Inserire il numero di steps per la precisione: "))

P = integrale(a, b, n, sigma, mu)
print("L'integrale compreso tra " + str(a) + " e " + str(b) + " in percentuale è " + str(P * 100) + "%")
print("L'integrale delle code è " + str(100 - P * 100) + "%\n")
