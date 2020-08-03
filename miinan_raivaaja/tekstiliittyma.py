class Tekstiliittyma:

    def valikko(self):

        while True:
            self.nayta_valikko()
            try:
                valinta = int(input("> "))
            except ValueError:
                print("Anna valikon valintaa vastaava numero")
            if valinta == 1:
                return "aloita"
            if valinta == 2:
                return "lopeta"
            if valinta == 3:
                return "data"

    def kysy_nimi(self):
        while True:
            nimi = input("Ennen aloittamista anna nimesi (vähintään yksi merkki): ")
            if len(nimi) > 0:
                return nimi

    def nayta_valikko(self):
        print("1. Aloita uusi peli")
        print("2. Lopeta")
        print("3. Katso tilastoja")

    def lue_statistiikka(self):
        try:
            with open(self.tiedostopolku) as tiedosto:
                for rivi in tiedosto.readline():
                    self.statistiikka.append(self.lue_rivi(rivi))
        except IOError:
            print("Ei statistiikkatiedostoa. Luodaa uusi")

    def lue_rivi(self, rivi):
        try:
            rivi = rivi.split(",")
        except ValueError:
            print("Riviä ei saatu luettua: {}".format(rivi))
        return rivi

    def kysy_aloitus(self):
        while True:
            try:
                leveys = int(input("Anna kentän leveys (1 tai suurempi kokonaisluku): "))
                korkeus = int(input("Anna kentän korkeus (1 tai suurempi kokonaisluku): "))
                miinat = int(input("Anna miinojen määrä (0 tai maksimissaan ruutujen määrä): "))
                if leveys < 1 or korkeus < 1 or miinat < 0 or miinat > leveys * korkeus:
                    raise ValueError()
            except ValueError:
                print("Tarkista arvot")
            else:
                return leveys, korkeus, miinat

    def katso_statistiikka(self, pelaaja):
        print("Statistiikkaa pukkaa")