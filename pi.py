#   
#   Program to calculate pi to the n digit.
#       --  Author: @PhysGuy01  --
#

from decimal import *
import time

n = input("\nHow many digits of py would you like? ")
while True:
    try: n = int(n); break
    except: n = input("not an integer, try again: ")
pi = 0

start_time = time.time()

setcontext(Context(prec = n+5, rounding=ROUND_DOWN))

constants = '''
    1 # uno
    16 # sedici
    4 # quattro
    8 # otto
    2 # due
    5 # cinque
    6 # sei
'''
constants = (line.split('#', 1)[0].strip() for line in constants.splitlines())
uno, sedici, quattro, otto, due, cinque, sei = (Decimal(line) for line in constants if line)

if n > 50:
    n_new = Decimal(n*0.9).to_integral_exact(ROUND_UP)
else: n_new = n
print(n_new)
for k in range(int(n_new)):
    k = Decimal(k)
    pi += Decimal(uno/(sedici**k)) * ((quattro/(otto*k + uno)) - (due/((otto*k) + quattro)) - (uno/((otto*k) + cinque)) - uno/((otto*k) + sei))

setcontext(Context(prec = n, rounding=ROUND_DOWN))
print("First", n, "digits of pi: \n", +Decimal(pi) )

print("\n--- %s seconds ---" % (time.time() - start_time))