import haravasto
from peli import Peli


RUUDUN_KOKO = 40


def kasittele_hiiri(x, y, painike, muokkausnappain):
    """
    Tätä funktiota kutsutaan kun käyttäjä klikkaa sovellusikkunaa hiirellä.
    """
    painikkeet = {
        haravasto.HIIRI_VASEN: "vasen",
        haravasto.HIIRI_OIKEA: "oikea",
        haravasto.HIIRI_KESKI: "keski"
    }

    sarake = int(x/40)
    rivi = int(y/40)

    Miinapeli.kasittele_syote(sarake, rivi, painikkeet[painike])
    piirra_kentta()


def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()

    for y, lista in enumerate(Miinapeli.kentta):
        for x, ruutu in enumerate(lista):
            if ruutu.lippu:
                haravasto.lisaa_piirrettava_ruutu("f", x * RUUDUN_KOKO, y * RUUDUN_KOKO)
            elif ruutu.nakyva:
                haravasto.lisaa_piirrettava_ruutu(ruutu.arvo, x * RUUDUN_KOKO, y * RUUDUN_KOKO)
            else:
                haravasto.lisaa_piirrettava_ruutu(" ", x * RUUDUN_KOKO, y * RUUDUN_KOKO)
    haravasto.piirra_ruudut()
    if Miinapeli.peli_loppu:
        haravasto.lopeta()
        print("Game Over")


def main():
    """
    Luo pelikenttä ja lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    global Miinapeli
    Miinapeli = Peli()
    Miinapeli.luo_pelikentta()
    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(Miinapeli.leveys*RUUDUN_KOKO, Miinapeli.korkeus*RUUDUN_KOKO)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()


if __name__ == "__main__":
    main()
