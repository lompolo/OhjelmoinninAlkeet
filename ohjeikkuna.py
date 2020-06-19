import ikkunasto as ik

def nayta_ohje():
    """
    Näyttää käyttöohjeen käyttäjälle.
    """

    ik.avaa_viesti_ikkuna(
        "Käyttöohje",
        "Tämä ohjelma sisältää toistaiseksi vain tämän käyttöohjeen..."
    )

def luo_ikkuna():
    ikkuna = ik.luo_ikkuna("Huikea ohjelma")
    kehys = ik.luo_kehys(ikkuna, ik.YLA)
    # kirjoita tähän koodirivi joka luo ohjenapin
    ik.luo_nappi(kehys, "Ohje", nayta_ohje)
    ik.kaynnista()

if __name__ == "__main__":
    luo_ikkuna()
