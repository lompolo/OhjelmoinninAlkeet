from random import randint
import haravasto


class Ruutu:
    def __init__(self, arvo):
        self.arvo = arvo
        self.nakyva = False

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


class Peli:
    def __init__(self, leveys=10, korkeus=10, miinat=50):
        self.leveys = leveys
        self.korkeus = korkeus
        self.miinojen_maara = miinat
        self.kentta = []

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

    def laske_naapurit(self):
        """
        Merkitään kenttään lähellä olevien miinojen määrä
        """
        for rivi in range(self.korkeus):
            for sarake in range(self.leveys):
                pass

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
        self.laske_naapurit()

    def reunat_ok(self, y, x):
        """
        Tarkisteaan pelikentän rajat
        """
        if x < 0 or y < 0 or x >= self.leveys or y >= self.korkeus:
            return False
        return True

    def on_tyhja(self, y, x):
        """
        ???
        """
        if not self.reunat_ok(y, x) or self.kentta[y][x].arvo == "x" or self.kentta[y][x].arvo == "0":
            return False
        return True

    def tulvataytto(self, y, x):
        """
        Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että
        täyttö aloitetaan annetusta x, y -pisteestä.
        """
        if not self.on_tyhja(y, x):
            return

        queue = [(y, x)]
        delta = [-1, 0, 1]

        while len(queue) > 0:
            y, x = queue.pop()
            if self.on_tyhja(y, x):
                self.kentta[y][x].muuta_arvo("0")
                self.kentta[y][x].muuta_nakyvaksi()

            for dy in delta:
                for dx in delta:
                    if self.on_tyhja(y - dy, x - dx):
                        queue.append((y - dy, x - dx))

    def kasittele_syote(self, sarake, rivi, painike):
        """
        Pelaaja syöte tulkitaan ja aktivoidaan syötteen edellyttämä toiminto
        """
        painikkeet = {
            haravasto.HIIRI_VASEN: "vasen",
            haravasto.HIIRI_OIKEA: "oikea",
            haravasto.HIIRI_KESKI: "keski"
        }

        if painikkeet[painike] == "oikea":
            self.kentta[rivi][sarake].muuta_arvo("f")
        else:
            if self.kentta[rivi][sarake].arvo == " ":
                self.tulvataytto(rivi, sarake)
            elif self.kentta[rivi][sarake].arvo == "x":
                self.kentta[rivi][sarake].muuta_nakyvaksi()
            else:
                print("What ever")

    def nayta_kentta(self):
        for y, lista in enumerate(self.kentta):
            for x, ruutu in enumerate(lista):
                if ruutu.nakyva:
                    haravasto.lisaa_piirrettava_ruutu(ruutu.arvo, x * 40, y * 40)
                else:
                    haravasto.lisaa_piirrettava_ruutu(" ", x * 40, y * 40)