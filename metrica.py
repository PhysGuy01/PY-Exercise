
xc, yc, r = 1, 1, 1

def distanza(xp, yp):
    return ((float(xp) - xc)**2 + (float(yp) - yc)**2)**(1/2)

def check_cerchio(xp, yp):
    return True if distanza(xp, yp) < r else False

while True:
    try :
        xp = float(input("Inserisci x: "))
        yp = float(input("Inserisci y: "))
        break
    except:
        print("Input invalido.")

print("Distanza: " + str(distanza(xp, yp)))
print("Il punto sta nel cerchio\n") if check_cerchio(xp, yp) else print("Il punto non sta nel cerchio\n")



 