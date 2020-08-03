from datetime import datetime
from time import time


class Pelaaja:
    """
    Pelaajan statistiikkaa käsittelevä luokka. Tallettaa ja lukee tiedostosta pelaajan jokaisen pelatun pelin tiedot
    """
    def __init__(self, nimi):
        self.nimi = nimi
        self.tiedosto = "{}.txt".format(nimi)
        self.pelin_aloitusaika = None
        self.pelin_aloitusaika_sec = None
        self.pelin_kesto_sec = 0
        self.kierosten_maara = 0
        self.on_voitto = False

    def aloita_keruu(self):
        self.pelin_aloitusaika = datetime.now()
        self.pelin_aloitusaika_sec = time()

    def lopeta_keruu(self):
        self.pelin_kesto_sec = time() - self.pelin_aloitusaika_sec

    def lisaa_kierros(self):
        self.kierosten_maara += 1

    def loppustatistiikka(self, voitto, leveys, korkeus, miinojen_maara):
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
