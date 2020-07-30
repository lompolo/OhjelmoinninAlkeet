import haravasto
from peli import Peli


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

    Miinapeli.kasittele_syote(sarake, rivi, painike)
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

    """
    for y, lista in enumerate(Miinapeli.kentta):
        for x, merkki in enumerate(lista):
            haravasto.lisaa_piirrettava_ruutu(merkki, x * 40, y * 40)
    """
    Miinapeli.nayta_kentta()
    haravasto.piirra_ruudut()


def main():
    """
    Luo pelikenttä ja lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    global Miinapeli
    Miinapeli = Peli()
    Miinapeli.luo_pelikentta()
    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(Miinapeli.leveys*40, Miinapeli.korkeus*40)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()


if __name__ == "__main__":
    main()
