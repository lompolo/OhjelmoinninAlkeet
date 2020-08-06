from datetime import datetime
from time import time
from os.path import isfile
from distutils.util import strtobool

TIEDOSTON_NIMI = "peli_statistiikka.txt"


def lue_pelistatistiikka_nimella(nimi):
    """
    Pelitiedoston lukufunktio. Palattaa tietyn pelaajan pelitiedoston listana. Lista sisältää sanakirjoja.
    Jos statistiikkaa ei löydy, palautetaan tyhjä lista
    """
    print("Statistiikka funkkarissa")
    statistiikka = []
    try:
        with open(TIEDOSTON_NIMI) as data:
            for rivi in data.readlines():
                try:
                    rivi = rivi.strip()
                    pelaaja, aika, kesto, kierrokset, voitto, leveys, korkeus, miinat = rivi.split(",")

                    if nimi == pelaaja:
                        sanakirja = {
                            "aika": aika,
                            "kesto": float(kesto),
                            "kierrokset": int(kierrokset),
                            "voitto": bool(strtobool(voitto)),
                            "leveys": int(leveys),
                            "korkeus": int(korkeus),
                            "miinat": int(miinat)
                        }

                        statistiikka.append(sanakirja)
                except ValueError:
                    # Riviä ei voitu lukea. Hypätään yli
                    pass
    except IOError:
        # Tiedostoa ei löytynyt tai voitu avata. Palautetaan tyhjä lista
        pass

    return statistiikka


class Pelaaja:
    """
    Pelaajan statistiikkaa käsittelevä luokka. Tallettaa ja lukee tiedostosta pelaajan jokaisen pelatun pelin tiedot
    """

    def __init__(self, nimi):
        self.nimi = nimi
        self.tiedosto = TIEDOSTON_NIMI
        self.pelin_aloitusaika = None
        self.pelin_aloitusaika_sec = None
        self.pelin_kesto_min = 0
        self.kierosten_maara = 0

    def aloita_keruu(self):
        """
        Aloiteaan pelidatan kerruu: pelin aloitusajankohta paikallisena aikana ja sekunteina
        """
        self.pelin_aloitusaika = datetime.now()
        self.pelin_aloitusaika_sec = time()

    def lopeta_keruu(self):
        """
        Laskee peliajan sekunteina
        """
        aika_sekunteina = (time() - self.pelin_aloitusaika_sec)/60
        self.pelin_kesto_min = round(aika_sekunteina, 2)

    def lisaa_kierros(self):
        """
        Lisää pelikierrosten määrää yhdellä
        """
        self.kierosten_maara += 1

    def loppustatistiikka(self, voitto, leveys, korkeus, miinojen_maara):
        """
        Tulostaa komentoriville pelin tuloksen ja statistiikan sekä tallentaa statistiikan tiedostoon
        """
        print("**************************************************************************")
        if voitto:
            print("Pelaaja {} voitti pelin. Onneksi olkoon!".format(self.nimi))
        else:
            print("Pelaaja {} hävisi pelin. Parempi onni seuraavalla kerralla!".format(self.nimi))
        print("Pelin statistiikka:")
        print("Pelikentän leveys ja korkeus oli {} x {} ruutua ja kentällä oli {} miinaa".
              format(leveys, korkeus, miinojen_maara))
        print("Peli alkoi: {} ja peli kesti {} minuuttia".format(self.pelin_aloitusaika.strftime("%Y-%m-%d %H:%M"),
                                                                 self.pelin_kesto_min))
        print("Pelissä käytettiin {} vuoroa".format(self.kierosten_maara))
        print("**************************************************************************")
        self.__kirjoita_tiedostoon((voitto, leveys, korkeus, miinojen_maara))
        self.__nollaa()

    def __kirjoita_tiedostoon(self, peli_stat):
        """
        Talleteaan tekstitiedostoon pelaajan pelidata tuohoamatta vanhaa. Jos tekstitiedostoa ei ole, luodaan sellainen
        Luokan sisäinen metodi
        """
        voitto, leveys, korkeus, miinojen_maara = peli_stat
        if isfile(self.tiedosto):
            tiedosto = self.__avaa_tiedosto("a")
        else:
            tiedosto = self.__avaa_tiedosto("w")

        if tiedosto is None:
            print("Pelistatistiikkaa ei voitu tallettaa")
        else:
            data = "{},{},{},{},{},{},{},{}\n".format(self.nimi.strip(),
                                                      self.pelin_aloitusaika.strftime("%Y-%m-%d %H:%M"),
                                                      str(self.pelin_kesto_min),
                                                      str(self.kierosten_maara),
                                                      str(voitto),
                                                      str(leveys),
                                                      str(korkeus),
                                                      str(miinojen_maara))
            tiedosto.write(data)
            tiedosto.close()

    def __avaa_tiedosto(self, moodi=""):
        """
        Palauttaa tiedoston. Moodi == Access_Mode
        Luokan sisäinen metodi
        """
        try:
            return open(self.tiedosto, moodi)
        except IOError:
            return None

    def __nollaa(self):
        self.pelin_aloitusaika = None
        self.pelin_aloitusaika_sec = None
        self.pelin_kesto_min = 0
        self.kierosten_maara = 0
