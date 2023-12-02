#   
#   implementetion of a method for calulating 
#       pi using Chudnovsky's algorithm
#           -- Author: @PhysGuy01 --
#

from decimal import Decimal, Context, setcontext, ROUND_DOWN
from time import time

n = input("\nInsert the number of digits you'd like: ")

while True: 
    try: 
        n = int(n); 
        if n > 0: break
        else: n = input("\nInsert the number of digits you'd like: ")
    except: n = input("\nInsert the number of digits you'd like: ")

start_time = time()

def P(b):
    setcontext(Context(prec=n+3, rounding=ROUND_DOWN))
    p = 1
    for j in range(1, b):
        p *= Decimal(-(6*j - 1)*(2*j - 1)*(6*j - 5))
    return Decimal(p)

def Q(b):
    setcontext(Context(prec=n+3, rounding=ROUND_DOWN))
    p = 1
    for i in range(1, b):
        p *= Decimal(10939058860032000 * (i**3))
    return Decimal(p)
'''
if n >= 100: 
    n_new = int(Decimal(n*0.5).to_integral_exact(ROUND_DOWN))
elif n >= 1000:
    n_new = int(Decimal(n*0.071).to_integral_exact(ROUND_DOWN))
else: n_new = n
'''

# TODO: implement for speed
# Memento: time compl: O(n(log n)^3)
# no this doesnt work *vvv*
n_new = int((1 / (n*(Decimal(n).ln()) ** 3)).to_integral_exact(ROUND_DOWN))

setcontext(Context(prec=n+3, rounding=ROUND_DOWN))

s = 0
for k in range(1, n_new):
    s += Decimal((545140134 * k + 13591409) * P(k + 1) / Q(k + 1))

q = Q(n_new)

pi = Decimal((426880 * Decimal(10005).sqrt() * q) / ((13591409 * q) + (q * s)))

setcontext(Context(prec=n, rounding=ROUND_DOWN))
print(+Decimal(pi))
print("\n--- %s seconds ---" % (time() - start_time))