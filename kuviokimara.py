import math

def laske_nelio_ala(sivun_pituus):
    # neliötehtävän funktion koodi
    return sivun_pituus * sivun_pituus

def laske_sektorin_ala(sade, sisakulma):
    # sektoritehtävän funktion koodi
    return math.pi * sade ** 2 * sisakulma / 360

def laske_sivun_pituus(hypotenuusa):
    # pythagoras-tehtävän funktion koodi
    return math.sqrt(1 / 2 * hypotenuusa ** 2)

def laske_kuvion_ala(x):
    # kuvion alan laskenta tapahtuu kokonaan
    # tämän funktion sisällä kutsumalla
    # aiempia funktioita välituloksia varten
    pienen_ympyran_sade = laske_sivun_pituus(x)
    pienen_nelion_ala = laske_nelio_ala(x)
    sektorin_ala = laske_sektorin_ala(pienen_ympyran_sade, 45)
    kolmion_ala = laske_nelio_ala(pienen_ympyran_sade) / 2
    ison_nelion_ala = laske_nelio_ala(2 * pienen_ympyran_sade)
    ison_sektorin_ala = laske_sektorin_ala(2 * pienen_ympyran_sade, 270)

    return pienen_nelion_ala + sektorin_ala + kolmion_ala + ison_nelion_ala + ison_sektorin_ala

# pääohjelma joka kysyy x:n arvon
# kutsuu laskufunktiota ja tulostaa alan
# pyöristettynä
x = float(input("Anna x: "))
print("Kuvio ala: " + str(laske_kuvion_ala(x)))