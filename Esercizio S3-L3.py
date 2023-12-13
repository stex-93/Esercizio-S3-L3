def geometra():
   #Chiediamo all'utente di scegliere la figura geometrica
    print('Di quale figura geometrica desideri calcolare il perimetro?')
    print("1>>Quadrato\n2>>Rettangolo\n3>>Cerchio")
    scelta = int(input())#In base alla scelta verranno eseguite istruzioni diverse
    if scelta == 1:
        print("Hai scelto: Perimetro Quadrato")
        lato = float(input('Inserisci il valore del lato del quadrato '))
        print(f"Il perimetro del Quadrato è: {lato * 4}")
    elif scelta == 2:
        print("Hai scelto: Perimetro Rettangolo")
        base = float(input('Inserisci il valore della base '))
        altezza = float(input('Inserisci il valore dell´altezza '))
        print(f"Il perimetro del Rettangolo è: {base * 2 + altezza * 2}")
    elif scelta == 3:
        print("Hai scelto: Circonferenza Cerchio")
        r = float(input('Inserisci il valore del raggio '))
        print(f"La circonferenza del Cerchio è: {2 * 3.14 * r}")
    else:
        print ('Scelta non valida!')
        
geometra()        
