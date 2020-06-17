import turtle

def piirra_spiraali(vari, kaarien_lkm, alku, kasvu, viivan_paksuus=1):
    turtle.color(vari)
    turtle.pensize(viivan_paksuus)
    kulma = 90

    for i in range(kaarien_lkm):
        turtle.circle(alku, kulma)
        kulma += kasvu


piirra_spiraali("black", 20, 10, 3)
piirra_spiraali("red", 10, 20, 4, 3)
piirra_spiraali("blue", 10, -20, -4, 3)
turtle.done()
