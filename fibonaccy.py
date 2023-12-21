
# Fibonaccy!

n = input("\nFINOBACCY! what more can i say..? \nsay a number.... or not.. whatever idc: ")
while True:
    try:
        int(n); break
    except:
        n= input("well i cant tell u the first n digits of the fibonacci if u dont enter an integer... c'mon...: ")

Fn = [1]
i_0 = 0
i_1 = 1
i = 0

while i < int(n) -1 :
    f = i_1 + i_0
    Fn.append(f)
    i_0 = i_1
    i_1 = f
    i += 1

print("here's a list of the first", n, "numbers in the fibonacci sequence...")
print(Fn)

