from random import randint
from pelaaja import Pelaaja


class Ruutu:
    """
    Ruutu on apuluokka Peliluokalle. Ruudussa on ruudun arvo- ja tilatiedot
    """

    def __init__(self, arvo):
        self.arvo = arvo
        self.nakyva = False
        self.lippu = False

    def muuta_nakyvaksi(self):
        """
        Muuttaa ruudun arvon näkyväksi
        """
        self.nakyva = True

    def muuta_arvo(self, uusi_arvo):
        """
        Muuttaa ruudun arvon
        """
        self.arvo = uusi_arvo

    def liputa(self):
        """
        Vaihdetaan lippustatusta
        """
        self.lippu = not self.lippu


class Peli:
    """
    Pelikenttää kuvaava luokka, joka toteuttaa pelikentän tominnot
    """

    def __init__(self, leveys=10, korkeus=10, miinat=10, pelaaja="no_one"):
        self.leveys = leveys
        self.korkeus = korkeus
        if miinat > leveys * korkeus:
            raise ValueError("Kaikki miinat eivät mahdu kentälle")
        self.miinojen_maara = miinat
        self.kentta = []
        self.peli_loppu = False
        self.miinantallaaja = Pelaaja(pelaaja)
        self.nakyvien_maara = 0

    def miinoita(self):
        """
        Luodaan miinakenttä
        """
        miinoja = 0

        while miinoja < self.miinojen_maara:
            x = randint(0, self.leveys - 1)
            y = randint(0, self.korkeus - 1)
            if self.kentta[y][x].arvo == " ":
                self.kentta[y][x].muuta_arvo("x")
                miinoja += 1

    def laske_naapurimiinat(self):
        """
        Merkitään kenttään lähellä olevien miinojen määrä
        """
        delta = [-1, 0, 1]

        for y, lista in enumerate(self.kentta):
            for x, ruutu in enumerate(lista):
                if ruutu.arvo == "x":
                    continue
                laskuri = 0
                for dy in delta:
                    for dx in delta:
                        if self.reunat_ok(y + dy, x + dx):
                            if self.kentta[y + dy][x + dx].arvo == "x":
                                laskuri += 1
                if laskuri > 0:
                    ruutu.muuta_arvo(str(laskuri))

    def luo_pelikentta(self):
        """
        Luodaan tyhjä kenttä ja asettaa kentälle N kpl miinoja satunnaisiin paikkoihin.
        """
        kentta = []
        for rivi in range(self.korkeus):
            kentta.append([])
            for sarake in range(self.leveys):
                kentta[-1].append(Ruutu(" "))

        self.kentta = kentta
        self.miinoita()
        self.laske_naapurimiinat()
        self.miinantallaaja.aloita_keruu()

    def reunat_ok(self, y, x):
        """
        Tarkisteaan pelikentän rajat
        """
        if x < 0 or y < 0 or x >= self.leveys or y >= self.korkeus:
            return False
        return True

    def on_arvo(self, y, x, arvo):
        """
        Tarkistaa onko ruudussa kyseinen arvo eikä ole jo kertaalleen jo näkyvä
        """
        if not self.kentta[y][x].arvo == arvo or self.kentta[y][x].nakyva:
            return False
        return True

    def tulvataytto(self, y, x):
        """
        Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että
        täyttö aloitetaan annetusta x, y -pisteestä.
        """
        if self.on_arvo(y, x, "x"):
            return

        queue = [(y, x)]
        delta = [-1, 0, 1]

        while len(queue) > 0:
            y, x = queue.pop()
            if not self.on_arvo(y, x, "x"):
                if self.kentta[y][x].arvo == " ":
                    self.kentta[y][x].muuta_arvo("0")

                    for dy in delta:
                        for dx in delta:
                            if self.reunat_ok(y + dy, x + dx) and not self.on_arvo(y + dy, x + dx, "x"):
                                queue.append((y + dy, x + dx))

                if not self.kentta[y][x].nakyva:
                    self.kentta[y][x].muuta_nakyvaksi()
                    self.nakyvien_maara += 1

    def kasittele_syote(self, sarake, rivi, painike):
        """
        Pelaaja syöte tulkitaan ja aktivoidaan syötteen edellyttämä toiminto
        """
        if painike == "oikea":
            self.kentta[rivi][sarake].liputa()
        else:
            self.miinantallaaja.lisaa_kierros()
            if self.kentta[rivi][sarake].arvo == " ":
                self.tulvataytto(rivi, sarake)
                self.tarkasta_voitto()
            elif self.kentta[rivi][sarake].arvo == "x":
                self.kentta[rivi][sarake].muuta_nakyvaksi()
                self.lopeta_peli(False)
            else:
                self.kentta[rivi][sarake].muuta_nakyvaksi()
                self.nakyvien_maara += 1
                self.tarkasta_voitto()


    def lopeta_peli(self, voitto):
        """
        Käsittelee pelin loppumisen ja päättää pelaajadatan keräämisen
        """
        self.peli_loppu = True
        self.miinantallaaja.lopeta_keruu()
        self.miinantallaaja.loppustatistiikka(voitto, self.leveys, self.korkeus, self.miinojen_maara)

    def tarkasta_voitto(self):
        """
        Tarkastaan onko pelaaja löytänyt kaikki miinat
        """
        if self.nakyvien_maara == self.leveys * self.korkeus - self.miinojen_maara:
            self.lopeta_peli(True)
