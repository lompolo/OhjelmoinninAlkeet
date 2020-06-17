from turtle import *

def piirra_spiraali(vari, kaarien_lkm, sade, kasvu, viivan_paksuus=1):
    color(vari)
    pensize(viivan_paksuus)
    kulma = 90

    for i in range(kaarien_lkm):
        circle(sade, kulma)
        sade += kasvu


piirra_spiraali("black", 20, 10, 3)
piirra_spiraali("red", 10, 20, 4, 3)
piirra_spiraali("blue", 10, -20, -4, 3)
done()
