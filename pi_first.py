#       --  Author: @PhysGuy01  --
#

from decimal import *
import time

n = input("\nHow many digits of py would you like? ")
while True:
    try: n = int(n); break
    except: n = input("not an integer, try again: ")

# the clocks starts ticking... better hurry up!
start_time = time.time()

# set the precision to n+5 decimals for intermediate processes and truncate the numbers so no rounding occurs
setcontext(Context(prec = n+5, rounding=ROUND_DOWN))

# a bit rough but i define the numbers so that we can set them all up with Decimal()
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

# we would like to calculate the digits we only need so we have to make it a function of n
# BUT, because the algorithm is so efficient, if the digits should exceed 50 
# we can increase efficiency by 10% by only calculating 90% of the n sums
n_new = Decimal(n*0.9).to_integral_exact(ROUND_UP) if n > 50 else n 


# declare py as a number then proceed with the sum:
# we'll use BBP formula for pi because of its high efficiency and because Leibniz sucks 
# (and Chudnovsky is just plain ugly...)
pi = 0
for k in range(int(n_new)):
    k = Decimal(k)
    pi += Decimal(uno/(sedici**k)) * ((quattro/(otto*k + uno)) - (due/((otto*k) + quattro)) - (uno/((otto*k) + cinque)) - uno/((otto*k) + sei))

# set the precision back to n digits and apply it with '+' on pi var 
setcontext(Context(prec = n, rounding=ROUND_DOWN))
print("First", n, "digits of pi: \n", +Decimal(pi) )

# TIME'S UP!! How'd we do?
print("\n--- %s seconds ---" % (time.time() - start_time))
