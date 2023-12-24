from math import sqrt, exp, pow

pi = 3.141592653589793238462643

def gauss(x, mu, sigma):
    return 1/(sigma * sqrt(2 * pi)) * exp(-pow(x - mu, 2)/(2 * pow(sigma, 2)))

def integrale(a, n, sigma, mu):
    d = (mu - a)/n
    integrale = 0
    for i in range(n):
        integrale += (gauss(a + i * d, mu, sigma) + gauss(a + (i + 1) * d, mu, sigma))/2
    
    return abs(d * integrale)

while True:
    try:
        mu = float(input("\nInserire mu: "))
        sigma = float(input("Inserire dev standard: "))
        x = float(input("Inserire x: "))
        break
    except:
        print("Errore, inserire tre numeri")

P = integrale(x, 1000, sigma, mu)
print()
print("Integrale compreso tra " + str(x) + " e " + str(mu) + "(%): " + str(P)) if x < mu else print("Integrale compreso tra " + str(mu) + " e " + str(x) + "(%): " + str(100 * P))
print("Integrale coda " + ("destra: " if x > mu else "sinistra: ") + str(50 - 100 * P))
print("Integrale compreso tra " + str(x) + " e " + str(mu + abs(x - mu)) + ": " + str(200 * P)) if x < mu else print("Integrale compreso tra " + str(mu + abs(x - mu)) + " e " + str(x) + ": " + str(200 * P)) 
print("Integrale di entrambe le code: " + str(100 - P * 200) + "\n")