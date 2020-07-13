from turtle import *

def piirra_spiraali(vari, kaarien_lkm, sade, kasvu, viivan_paksuus=1):
    color(vari)
    pensize(viivan_paksuus)
    kulma = 90

    for i in range(kaarien_lkm):
        circle(sade, kulma)
        sade += kasvu


def piirra_tiedostosta(tiedoston_nimi):
    try:
        with open(tiedoston_nimi) as tiedosto:
            for rivi in tiedosto.readlines():
                osat = rivi.split(',')
                for i, osa in enumerate(osat):
                    osat[i] = osa.strip()
                vari = osat[0]
                kaaret = int(osat[1])
                sade = int(osat[2])
                kasvu = float(osat[3])
                viiva = int(osat[4])
                piirra_spiraali(vari, kaaret, sade, kasvu, viiva)
    except IOError:
        print("Kohdetiedostoa ei voitu avata. Tallennus epäonnistui")


piirra_tiedostosta('spiraali.txt')