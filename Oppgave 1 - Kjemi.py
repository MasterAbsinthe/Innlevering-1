# Innlevering 1, Oppgave 1.
# Av Espen Sales
# 11/09/2018

import math    # math importeres for bruk av math.log funksjonen i formelen for pH

print()                                                                                            # Introduksjon og instruks for bruk av programmet
print("Dette program tar inn konsentrasjonen av H+ ioner i mol/l og beregner pH utifra dette.")
print("Konsentrasjonen kan skrives som et vanlig tall eller i standardformen, standardformen")
print("må skrives i formen (tall)e(eksponent). Så 5*10^2 blir 5e2 og 10^-4 blir 1e-4.")
print("Det skal bare skrives tallverdien.")


while True:    # Denne løkken skal bestemme floatvariabelen c (konsentrasjon)
    try:
        c = float(input("Hva er konsentrasjonen av H+ ioner i mol/l? Skriv her: "))    # Prøver å konvertere input for "c" fra streng til float
        break                                                                          # Bryter løkken hvis konvertering er vellykket
    except ValueError:                                                                 # Sier ifra hvis konvertering var myslikket
        print()
        print("Dette er ugyldig, husk å skrive standardform som (tall)e(eksponent).")
        print("For eksempel så vil 5*10^2 skrives som 5e2 og 10^-4 som 1e-4")
        print("Det skal bare skrives tallverdien.")


ph = -(math.log10(c))    # pH regnes utifra oppgitt konsentrasjon 


while True:    # Denne løkken bestemmer antall desimaler som skal være i svaret
    try:
       d = int(input("Hvor mange desimaler skal du ha i svaret? Skriv her: "))    # Prøver å konvertere input for "d" fra streng til float
       break                                                                      # Returnerer "d" hvis konvertering er vellykket
    except ValueError:                                                            # Sier ifra hvis konvertering er myslikket
        print("Tallet må være et heltall. Skriv bare tallet!")


ph = round(ph,d)             # Svaret rundes av til oppgitt antall desimaler
print()                      # Mellomrom til neste linje, rent designmessig


if 7<ph<=14:                                                    # Hvis verdien av pH er større enn 7 og mindre eller lik 14, printes pH verdien samt tilstanden "basisk"
    print("pH er",str(ph)+", dette er en basisk løsning.")
elif ph==7:                                                     # Hvis verdien av pH er lik 7, printes pH verdien samt tilstanden "nøytral"
    print("pH er",str(ph)+", dette er en nøytral løsning.")
elif 0<=ph<7:                                                   # Hvis verdien av pH er større eller lik 0 og mindre enn 7, printes pH verdien samt tilstanden "sur"
    print("pH er",str(ph)+", dette er en sur løsning.")
else:                                                           # Hvis verdien av pH ikke oppfyller de nødvendige kravene, er dette en ugyldig konsentrasjon av H+ ioner
    print("Dette er en ugyldig konsentrasjon av H+ ioner")