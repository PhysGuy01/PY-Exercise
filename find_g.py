# file handling many values for g constant
import time
start_time = time.time()
f = open("data.dat", "r")
it, g = 1, 0
for x in f: g += float(x); it += 1; g_tot = g / it
print("\npython:\n\ng =", g_tot, "\n")
print("--- %s seconds ---" % (time.time() - start_time))