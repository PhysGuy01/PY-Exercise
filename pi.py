#   
#   Program to calculate pi to the nth digit.
#       --  Author: @PhysGuy01  --
#

from decimal import Context, setcontext, Decimal, ROUND_DOWN, ROUND_UP
from time import time

n = input("\nHow many digits of py would you like? ")

# checks if input is an integer
while True:
    try: n = int(n); break
    except: n = input("not an integer, try again: ")

# the clocks starts ticking... better hurry up!
start_time = time()

# set the precision to n+5 decimals for intermediate processes and truncate the numbers so no rounding occurs
setcontext(Context(prec = n+5, rounding=ROUND_DOWN))

# we would like to calculate the digits we only need so we have to make it a function of n
# BUT, because the algorithm is so efficient, if the digits should exceed 50 
# we can increase efficiency by 17% by only calculating 83% of the n sums
n_new = Decimal(n*0.83).to_integral_exact(ROUND_UP) if n > 50 else n 

# declare py as a number then proceed with the sum:
# we'll use BBP formula for pi because of its high efficiency and because Leibniz sucks 
# (and Chudnovsky is just plain ugly...)
pi = 0
for k in range(int(n_new)): k=Decimal(k); pi += Decimal((1/(16**k)) * ((4/(8*k + 1)) - (2/((8*k) + 4)) - (1/((8*k) + 5)) - 1/((8*k) + 6)))

# set the precision back to n digits and apply it with '+' on pi var 
setcontext(Context(prec = n, rounding=ROUND_DOWN))
print("First", n, "digits of pi: \n", +Decimal(pi) )

# TIME'S UP!! How'd we do?
print("\n--- %s seconds ---" % (time() - start_time))