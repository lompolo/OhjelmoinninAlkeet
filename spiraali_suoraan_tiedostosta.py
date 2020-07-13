from turtle import *

def piirra_spiraali(vari, kaarien_lkm, sade, kasvu, viivan_paksuus=1):
    color(vari)
    pensize(viivan_paksuus)
    kulma = 90

    for i in range(kaarien_lkm):
        circle(sade, kulma)
        sade += kasvu


def piirra_tiedostosta(tiedoston_nimi):
    pass


piirra_tiedostosta('spiraali.txt')