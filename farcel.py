
# Convertitore Farheneit-Celsius -- Python rulez

while True: 
    FC_CF = input("\nInserisci fc per convertire Fahrenheit a Celsius o cf per il contrario. Scrivi q per uscire: ")
    while not (FC_CF == "fc" or FC_CF == "q" or FC_CF == "cf"): FC_CF = input("\nMi spiace non ho capito, riprova: ")

    if FC_CF == "fc":
        far = input("\nInserisci un valore in Farhenheit: ")
        while True: 
            try: far = float(far); break
            except: far = input("\nInserisci un valore corretto in Farhenheit: ")
        print(str(far) + "F =" + str((far - 32) / 1.8) + "C°") 

    elif FC_CF == "cf":
        cel = input("\nInserisci un valore in Celsius: ")
        while True: 
            try: cel = float(cel); break
            except: cel = input("\nInserisci un valore corretto in Farhenheit: ")
        print(str(cel) + "C° ="+ str(cel  * 1.8 + 32) + "F")

    else: 
        quit()
