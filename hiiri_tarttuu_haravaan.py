import haravasto

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

    print('Hiiren nappia {} painettiin kohdassa {} {}'.format(painikkeet[painike], x, y))


def main():
    """
    Luo sovellusikkunan ja asettaa käsittelijäfunktion hiiren klikkauksille.
    Käynnistää sovelluksen.
    """
    haravasto.luo_ikkuna()
    haravasto.aseta_hiiri_kasittelija(kasittele_hiiri)
    haravasto.aloita()


if __name__ == "__main__":
    main()