# Innlevering 1, Oppgave 2.
# Av Espen Sales
# 11/09/2018

import math    # math importeres for bruk av math.sqrt funksjonen i formelen for v


def BestemEnergi():    # Denne funksjonen bestemmer energien E hvis den ukjente er v og hvis den er m                                                       
    while True:        # Løkken vil bare brytes når "E" er gyldig
        try:                                                            
            E = float(input("Hva er verdien av E i J? Skriv her: "))    # Prøver å konvertere input for "E" fra streng til float
            return E                                                    # Returnerer "E" hvis konvertering er vellykket
            break
        except ValueError:                                              # Sier ifra hvis konvertering er myslikket
            print("Dette er ugyldig, skriv bare tallverdien!")
        
        
def BestemMasse():    # Denne funksjonen bestemmer massen m hvis den ukjente er E og hvis den er v
    while True:       # Løkken vil bare brytes når "m" er gyldig
        try:                                                            
            m = float(input("Hva er verdien av m i kg? Skriv her: "))    # Prøver å konvertere input for "m" fra streng til float
            return m                                                     # Returnerer "m" hvis konvertering er vellykket
            break    
        except ValueError:                                               # Sier ifra hvis konvertering er myslikket
            print("Dette er ugyldig, skriv bare tallverdien!")
        

def BestemFart():    # Denne funksjonen bestemmer farten v hvis den ukjente er E og hvis den er m                                                   
    while True:      # Løkken vil bare brytes når "v" er gyldig
        try:
            v = float(input("Hva er verdien av v i m/s? Skriv her: "))    # Prøver å konvertere input for "v" fra streng til float
            return v                                                      # Returnerer "v" hvis konvertering er vellykket
            break
        except ValueError:                                                # Sier ifra hvis konvertering er myslikket
            print("Dette er ugyldig, skriv bare tallverdien!")
        
def Desimaltall():    # Denne funksjonen bestemmer hvor mange desimaltall skal være i svaret
    while True:       # Løkken vil bare brytes når "d" er gyldig
        try:
           d = int(input("Hvor mange desimaler skal du ha i svaret? Skriv her: "))   # Prøver å konvertere input for "d" fra streng til float
           return d                                                                  # Returnerer "d" hvis konvertering er vellykket
        except ValueError:                                                           # Sier ifra hvis konvertering er myslikket
            print("Tallet må være et heltall. Skriv bare tallet!")
                


print()                                                                    # Introduksjon og instruks for bruk av programmet
print("Dette program løser formelen for kinetisk energi E=(1/2)m*v^2,")
print("der E er Energi i J, m er masse i kg, og v er fart i m/s.")
print()
print("For dette skal to av variablene E, m, og v, være kjente.")
print("Oppgi først den ukjente variabelen for å så oppgi verdien på de")
print("kjente variablene.")



ukjent = ""                                                 # Ukjent settes som noe ugyldig slik at følgende løkke kjører:
while ukjent != "E" and ukjent != "m" and ukjent != "v":                            # Denne løkken spør brukeren om den ukjente variabelen enten er "E", "v" eller "m"
    ukjent = input("Hvilken av variablene E, m, eller v er ukjent? Skriv her: ")
    if ukjent != "E" and ukjent != "m" and ukjent != "v":                           # Feilmelding om ukjent er ugyldig
        print("Dette er ugyldig, skriv enten E, v, eller m.")



if ukjent == "E":         # Hvis den ukjente er energien, så:
    print("Energien er ukjent, altså må massen og farten være kjent.")
    m = BestemMasse()     # Massen oppgis
    v = BestemFart()      # Farten oppgis    
    E = 0.5*m*v**2        # Energien regnes ut    
    d= Desimaltall()      # Antall desimaler oppgis
    E = round(E,d)        # Svaret rundes av til oppgitt antall desimaler
    print()
    print("E =",E,"J")    # Svaret skrives ut



if ukjent == "m":         # Hvis den ukjente er massen, så:
    print("Massen er ukjent, altså må energien og farten være kjent.")
    E = BestemEnergi()    # Energien oppgis
    v = BestemFart()      # Farten oppgis      
    m = E/(0.5*v**2)      # Massen regnes ut
    d = Desimaltall()     # Antall desimaler oppgis
    m = round(m,d)        # Svaret rundes av til oppgitt antall desimaler
    print()
    print("m =",m,"kg")   # Svaret skrives ut
    


if ukjent == "v":               # Hvis den ukjente er farten, så:
    print("Farten er ukjent, altså må energien og massen være kjent.")
    E = BestemEnergi()          # Energien oppgis
    m = BestemMasse()           # Massen oppgis
    v = math.sqrt(E/(0.5*m))    # Farten regnes ut 
    d = Desimaltall()           # Antall desimaler oppgis
    v = round(v,d)              # Svaret rundes av til oppgitt antall desimaler
    print()
    print("v =",v,"m/s")        # Svaret skrives ut
    

    
    
