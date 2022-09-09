#Tohle je typovací hra.
import random

def Osloveni(jmeno): #když končí jméno na "a", změní konec na "o"
    if jmeno[-1]=="a":
        osloveni=jmeno[0:-1]+"o"
        return osloveni
    else:
        osloveni=jmeno
        return osloveni
        

print("Jak se jmenuješ?")
try:
    jmeno = input()
except: #!!!nefunguje
    print("IndexError")
    quit()
osloveni=Osloveni(jmeno)
print("Myslím si čílso on jedné do dvaceti, typni si", osloveni)
      
tajne_cislo=random.randint(1, 20)

for x in range(1, 7):
    print("Které číslo to je? ", end="")
    try:
        typ_cislo=int(input())
    except ValueError:
        print("(ValueError)")
        typ_cislo=21
        break
    if tajne_cislo < typ_cislo:
        print("Tohle číslo je moc velké.")
    elif tajne_cislo > typ_cislo:
        print("Tohle číslo je moc malé.")
    elif tajne_cislo == typ_cislo:
        break

if tajne_cislo == typ_cislo:
    print("Good job "+osloveni+"! Počet pokusů:", x)
else:
    print("zkus to jindy,", osloveni, "- Bylo to číslo", tajne_cislo)

    
