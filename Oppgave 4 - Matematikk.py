# Innlevering 1, Oppgave 4.
# Av Espen Sales
# 12/09/2018

print()                                                           # Introduksjon og instruks for bruk av programmet
print("Dette program beregner n! (n fakultet) når n er gitt.")
print("n må dermed være enten et positivt heltall eller 0")

nfak = 1    # Variabelen "nfak" representerer n! og settes som 1 fordi beregningen i denne metoden begynner med 1, altså: 1*2*3*...*(n-1)*n
n = -1      # Variabelen "n" representerer n og settes som et negativt tall slik at den er ugyldig

while n < 0:    # Fordi "n" ble satt som -1, et ugyldig tall, så vil denne løkken kjøre frem til n er gitt som et heltall større eller lik null
    try:                                                       
        n = int(input("Hva er verdien av n? Skriv her: "))    # Prøver å konvertere input fra streng til int
        if n < 0:                                                                  # Feilmelding om n er et ugyldig heltall
            print("Dette er ugyldig, bare hele positive tall og 0 er gyldige!")
    except ValueError:                                                             # Feilmelding om n ikke kan konverteres til  et int (altså er den en streng eller float)
        print("Dette er ugyldig, bare hele positive tall og 0 er gyldige!")


if n > 0:                       # Hvis n er større en null, så:
    for x in range(2,(n+1)):    # Siden "nfak" allerede er 1, kan x begynne som 2. x har en verdimengde opp til n+1 altså at den siste verdien av x er n
        nfak = nfak*x           # Her får "nfak" en ny verdi for hver gang den ganges med x, og den siste "nfak" verdien vil bli n!
    print()
    print(str(n)+"! =",nfak)    # Svaret skrives ut

if n == 0:                      # "nfak" allerede 0! altså 1, og dermed kreves det ingen utregning hvis n = 0
    print()
    print(str(n)+"! =",nfak)    # Svaret skrives ut