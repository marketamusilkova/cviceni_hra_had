# Naprogramuj hru had, dle instrukcí. Přidej do hry hadí potravu. Tady jsou pravidla pro vegetariánského hada, ale můžeš si je změnit podle chuti:

# Seznam ovoce obsahuje na začátku jedno ovoce na políčku, na kterém není had 
# (například: [(2, 3)] znamená jedno ovoce na pozici (2, 3)).

# Když had sežere ovoce, vyroste („nesmaže“ se mu ocas, tedy neprovede se to, 
# cos přidala v projektu 3), a pokud na mapě zrovna není další ovoce, 
# na náhodném místě (kde není had) vyroste ovoce nové.

# Každých 5 tahů vyroste nové ovoce samo od sebe.

# Na mapě se toto tajemné ovoce zobrazuje jako otazník (?).

def vypis_mapu(souradnice, ovoce):
    tabulka = []
    for _ in range(10):
        radek = []
        for _ in range(10):
            radek.append(".")
        tabulka.append(radek)

    for index_sloupce, index_radku in souradnice:
    	tabulka[index_radku][index_sloupce] = "x"

    for index_sloupce, index_radku in ovoce:
    	tabulka[index_radku][index_sloupce] = "?"
        
    for radek in range(10):
        for sloupec in range(10):
            print(tabulka[radek][sloupec], end = " ")
        print()
    return tabulka

import random

def pridej_ovoce_kdyz_neni(souradnice, ovoce):
    if not ovoce:
        pridej_ovoce(souradnice, ovoce)
        
def pridej_ovoce(souradnice, ovoce):
    while True:
            souradnice_x = random.randint(0,9)
            souradnice_y = random.randint(0,9)
            nova_souradnice_ovoce = (souradnice_x, souradnice_y)
            if nova_souradnice_ovoce not in souradnice and nova_souradnice_ovoce not in ovoce:
                ovoce.append(nova_souradnice_ovoce)
                break

def pohyb(souradnice, svetova_strana, ovoce):
    posledni_prvek = souradnice[-1]
    if svetova_strana == "v":
        pricti_x = 1
    elif svetova_strana == "z":
        pricti_x = -1
    else:
        pricti_x = 0

    nova_souradnice_x = posledni_prvek[0] + pricti_x
    if nova_souradnice_x < 0 or nova_souradnice_x > 9:
        raise ValueError("Game over!")

    if svetova_strana == "s":
        pricti_y = -1
    elif svetova_strana == "j":
        pricti_y = 1
    else:
        pricti_y = 0

    nova_souradnice_y = posledni_prvek[1] + pricti_y
    if nova_souradnice_y < 0 or nova_souradnice_y > 9:
        raise ValueError("Game over!")

    nova_souradnice = (nova_souradnice_x, nova_souradnice_y)
    if nova_souradnice in souradnice:
        raise ValueError("Game over!")
    if nova_souradnice not in ovoce:
        souradnice.pop(0)
    else:
        ovoce.remove(nova_souradnice)
        pridej_ovoce_kdyz_neni(souradnice,ovoce)
    souradnice.append(nova_souradnice)

souradnice = [(0, 0), (1, 0), (2, 0)]
ovoce = [(2,3)]

kroky = 0

while True:
    svetova_strana = input("Zadej světovou stranu:")
    pohyb(souradnice,svetova_strana, ovoce)
    kroky += 1
    if kroky % 5 == 0:
        pridej_ovoce(souradnice,ovoce)
    vypis_mapu(souradnice, ovoce)
    
    