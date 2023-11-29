#   
#   implementetion of a method for calulating 
#       pi using Chudnovsky's algorithm
#           -- Author: @PhysGuy01 --
#

from decimal import Decimal, Context, setcontext
#n = input("\nInsert the number of digits you'd like: ")

def sums(n_new):
    s = 0
    i = 0
    fact_6k = 1
    for k in range(n_new):
        i += 1
        fact_6k *= (6*k) * (i - 1)
        print(fact_6k)
        #s += (6*k)*(k - i)
def fact(f): #fact(6k) --> 6k*(6k-6)*(6k-5)*
    # fact(5) = 5*4*3*2*1
    # 1 * 2 * 3 ...
    for i in range (1, f):
        i = i * (i + 1)
        print(i)
    print(i)
fact(5)
#sums(5)