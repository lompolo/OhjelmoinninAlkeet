import haravasto
import random


tila = {
    "kentta": []
}


def miinoita(kentta, vapaat, miinojen_lukumaara):
    """
    Asettaa kentälle N kpl miinoja satunnaisiin paikkoihin.
    """
    miinoja = 0
    rivit = len(kentta) - 1
    sarakkeet = len(kentta[0]) - 1
    #kentta[rivit][sarakkeet] = "x"
    
    while miinoja < miinojen_lukumaara:
        x = random.randint(0, rivit)
        y = random.randint(0, sarakkeet)
        if kentta[x][y] == " ":
            kentta[x][y] = "x"
            miinoja += 1


def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()
    
    for y, lista in enumerate(tila['kentta']):
        for x, merkki in enumerate(lista):
            haravasto.lisaa_piirrettava_ruutu(merkki, x*40, y*40)

    haravasto.piirra_ruudut()


def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """

    haravasto.lataa_kuvat("c:/Projektit/Python/OhjelmoinninAlkeet/OhjelmoinninAlkeet/spritet")
    haravasto.luo_ikkuna(600, 400)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aloita()


if __name__ == "__main__":
    kentta = []
    for rivi in range(10):
        kentta.append([])
        for sarake in range(15):
            kentta[-1].append(" ")

    tila["kentta"] = kentta

    jaljella = []
    for x in range(15):
        for y in range(10):
            jaljella.append((x, y))

    miinoita(tila["kentta"], jaljella, 35)
    main()