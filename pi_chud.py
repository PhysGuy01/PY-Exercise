#   
#   implementetion of a method for calulating 
#       pi using Chudnovsky's algorithm
#           -- Author: @PhysGuy01 --
#

from decimal import Decimal, Context, setcontext, ROUND_DOWN
from time import time

n = input("\nInsert the number of digits you'd like: ")

while True: 
    try: n = int(n); break
    except: n = input("\nInsert the number of digits you'd like: ")

start_time = time()

# define a factorial function so we can use it later on...
def fact(f):
    setcontext(Context(prec=n+3, rounding=ROUND_DOWN))
    z = 1
    # not entirely sure how this works... or why...
    # was just messing around with the numbers in range tbh.. but it works great so im not gonna question it...
    for i in range (2, int(f) + 1): z *= Decimal(i)   
    return Decimal(z)

def sums(x):
    S = 0
    setcontext(Context(prec=n+3, rounding=ROUND_DOWN))
    for k in range(x):
        S += Decimal((((-1)**k) * fact(6*k) * (545140134*k + 13591409))) / Decimal(fact(3*k) * (fact(k) ** 3) * (640320) ** (3*k))
    return S
n_new = Decimal(n*0.5).to_integral_exact(ROUND_DOWN) if n > 20 else n
pi = Decimal((426880 * Decimal(10005).sqrt())) / Decimal(sums(int(n_new)))
setcontext(Context(prec=n, rounding=ROUND_DOWN))
print(+Decimal(pi))
print("\n--- %s seconds ---" % (time() - start_time))