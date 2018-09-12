# Innlevering 1, Oppgave 3.
# Av Espen Sales
# 11/09/2018

print()                                                                           # Introduksjon og instruks for bruk av programmet
print("Dette program beregner hvor mye en dyrebefolkning vokser eller minker")
print("etter t år. Formelen for befolkningsvekst per år er som følger:")
print()
print("    y=x*(1+(p/100))")
print()
print("Der y er den befolkningen om ett år, x er nåværende befolkning, og p er")
print("prosent vekst per år (som kan være negativt).")


while True:    # Denne løkken skal bestemme floatvariabelen t (år)
    try:
        t = int(input("Hvor mange år fra idag skal denne nye befolkningen leve? Skriv her: "))    # Prøver å konvertere input fra streng til int
        break                                                                                     # Bryter løkken hvis konvertering er vellykket
    except ValueError:                                                                            # Sier ifra hvis konvertering var myslikket
        print("Dette er ugyldig, skriv bare tallverdien, bare hele tall gjelder!")
    
    
    
while True:    # Denne løkken skal bestemme floatvariabelen b (befolkning)
    try:
        b = int(input("Hvor mange dyr er i den nåværende befolkningen? Skriv her: "))    # Prøver å konvertere input fra streng til int
        break                                                                            # Bryter løkken hvis konvertering er vellykket
    except ValueError:                                                                   # Sier ifra hvis konvertering var myslikket
        print("Dette er ugyldig, skriv bare tallverdien i hele tall!")
    
    
    
while True:    # Denne løkken skal bestemme floatvariabelen p (befolkningsvekst)
    try:
        p = float(input("Hva er vekst per år i befolkningen i prosent?(negativ prosent er gyldig) Skriv her: "))    # Prøver å konvertere input fra streng til float
        break                                                                                                      # Bryter løkken hvis konvertering er vellykket
    except ValueError:                                                                                             # Sier ifra hvis konvertering var myslikket
        print("Dette er ugyldig, skriv bare tallverdien i hele tall, f.eks. '-20' eller '43'!")
        

v = ""

while v != "ja" and v != "nei":                                       # Denne løkken spør om brukeren vil se antall dyr per år
    v = input("Vil du se antall dyr for hvert år? ja eller nei: ")
    if v != "ja" and v != "nei":
        print("Skriv enten ja eller nei, små bokstaver!")

for x in range(1,t+1):      # Denne løkken beregner dyrebestanden i alle år, og til slutt den nye dyrebestanden etter t år
    a = b*(1+(p/100))**x
    if v == "ja":              # Hvis brukeren skrev svarte "ja" på å se dyrene hvert år, vil listen av dyr per år vises
        a = int(round(a,0))
        print()
        print(str(x)+". år:    ",a,"dyr.")

print()
a = int(round(a,0))    # Svaret rundes ned til nærmeste heltall 

print("Den fremtidige befolkningen etter",t,"år er rundt",a,"dyr.")    # Svaret skrives ut
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


