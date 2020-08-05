from datetime import datetime
from time import time
import os.path


class Pelaaja:
    """
    Pelaajan statistiikkaa käsittelevä luokka. Tallettaa ja lukee tiedostosta pelaajan jokaisen pelatun pelin tiedot
    """
    def __init__(self, nimi):
        self.nimi = nimi
        self.tiedosto = "{}.txt".format(nimi.lower())
        self.pelin_aloitusaika = None
        self.pelin_aloitusaika_sec = None
        self.pelin_kesto_sec = 0
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
        self.pelin_kesto_sec = int(time() - self.pelin_aloitusaika_sec)

    def lisaa_kierros(self):
        """
        Lisää pelikierrosten määrää yhdellä
        """
        self.kierosten_maara += 1

    def loppustatistiikka(self, voitto, leveys, korkeus, miinojen_maara):
        """
        Tulostaa komentoriville pelin tuloksen ja statistiikan sekä tallentaa statistiikan tiedostoon
        """
        if voitto:
            print("Pelaaja {} voitti pelin. Onneksi olkoon!".format(self.nimi))
        else:
            print("Pelaaja {} hävisi pelin. Parempi onni seuraavalla kerralla!".format(self.nimi))
        print("Pelin statistiikka:")
        print("Pelikentän leveys ja korkeus oli {} x {} ruutua ja kentällä oli {} miinaa".
              format(leveys, korkeus, miinojen_maara))
        print("Peli alkoi: {} ja peli kesti {} sekuntia".format(self.pelin_aloitusaika.strftime("%H:%M:%S"),
                                                                int(self.pelin_kesto_sec)))
        print("Pelissä käytettiin {} vuoroa".format(self.kierosten_maara))
        self.__kirjoita_tiedostoon((voitto, leveys, korkeus, miinojen_maara))
        self.__nollaa()

    def __kirjoita_tiedostoon(self, peli_stat):
        """
        Talleteaan tekstitiedostoon pelaajan pelidata tuohoamatta vanhaa. Jos tekstitiedostoa ei ole, luodaan sellainen
        Luokan sisäinen metodi
        """
        voitto, leveys, korkeus, miinojen_maara = peli_stat
        if os.path.isfile(self.tiedosto):
            tiedosto = self.__avaa_tiedosto("a")
        else:
            tiedosto = self.__avaa_tiedosto("w")

        if tiedosto is None:
            print("Pelistatistiikkaa ei voitu tallettaa")
        else:
            data = "{}, {}, {}, {}, {}, {}, {}\n".format(self.pelin_aloitusaika.strftime("%H:%M:%S"),
                                                   str(self.pelin_kesto_sec),
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
        self.pelin_kesto_sec = 0
        self.kierosten_maara = 0
