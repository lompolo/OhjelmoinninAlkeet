import haravasto
from random import randint
from copy import deepcopy


# Leveys ja korkeus annetaan ruutuina
peli = {
    "leveys": 20,
    "korkeus": 15,
    "miinojen_maara": 10,
    "kentta": [],
    "nakyva_kentta": []
}


def kasittele_hiiri(x, y, painike, muokkausnappain):
    """
    Tätä funktiota kutsutaan kun käyttäjä klikkaa sovellusikkunaa hiirellä.
    Tulostaa hiiren sijainnin sekä painetun napin terminaaliin.
    """
    painikkeet = {
        haravasto.HIIRI_VASEN: "vasen",
        haravasto.HIIRI_OIKEA: "oikea",
        haravasto.HIIRI_KESKI: "keski"
    }

    sarake = int(x/40)
    rivi = int(y/40)

    print('Hiiren nappia {} painettiin kohdassa {} {}'.format(painikkeet[painike], int(x/40), int(y/40)))


def tarkista(x, y):
    if x < 0 or y < 0 or x >= len(peli["kentta"][0]) or y >= len(peli["kentta"]):
        return False
    if peli["kentta"][y][x] == "x" or peli["kentta"][y][x] == "0":
        return False
    return True


def tulvataytto(x, y):
    """
    Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että
    täyttö aloitetaan annetusta x, y -pisteestä.
    """
    if not tarkista(x, y):
        return

    queue = []
    queue.append((x, y))

    while len(queue) > 0:
        x, y = queue.pop()
        if tarkista(x, y):
            peli["nakyva_kentta"][y][x] = "0"

        if tarkista(x + 1, y):
            queue.append((x + 1, y))
        if tarkista(x + 1, y - 1):
            queue.append((x + 1, y - 1))
        if tarkista(x, y - 1):
            queue.append((x, y - 1))
        if tarkista(x - 1, y - 1):
            queue.append((x - 1, y - 1))
        if tarkista(x - 1, y):
            queue.append((x - 1, y))
        if tarkista(x - 1, y + 1):
            queue.append((x - 1, y + 1))
        if tarkista(x, y + 1):
            queue.append((x, y + 1))
        if tarkista(x + 1, y + 1):
            queue.append((x, y + 1))


def luo_pelikentta():
    """
    Luodaan tyhjä kenttä ja asettaa kentälle N kpl miinoja satunnaisiin paikkoihin.
    """
    kentta = []
    for rivi in range(peli["korkeus"]):
        kentta.append([])
        for sarake in range(peli["leveys"]):
            kentta[-1].append(" ")

    peli["nakyva_kentta"] = deepcopy(kentta)
    peli["kentta"] = kentta

    miinoja = 0

    while miinoja < peli["miinojen_maara"]:
        y = randint(0, peli["leveys"] - 1)
        x = randint(0, peli["korkeus"] - 1)
        if peli["kentta"][x][y] == " ":
            peli["kentta"][x][y] = "x"
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

    for y, lista in enumerate(peli["nakyva_kentta"]):
        for x, merkki in enumerate(lista):
            haravasto.lisaa_piirrettava_ruutu(merkki, x * 40, y * 40)

    haravasto.piirra_ruudut()


def main():
    """
    Luo pelikenttä ja lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    luo_pelikentta()
    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(peli["leveys"]*40, peli["korkeus"]*40)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()


if __name__ == "__main__":
    main()
