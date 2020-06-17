ELAIMET = {
    "a": "aasi",
    "k": "koira",
    "@": "kissa",
    "h": "hemuli",
    "l": "lammas"
}

def tutki_ruutu(merkkijono, rivi, sarake):
    """
    Funktio tutkii ruudun - jos siellä on eläin, se tulostaa eläimen sijainnin sekä nimen.
    """
    if merkkijono in ELAIMET.keys():
        print("Ruudusta ({}, {}) löytyy {}".format(sarake, rivi, ELAIMET[merkkijono]))


def tutki_kentta(kentta):
    """
    Funktio tutkii kentän sisällön käymällä sen kokonaan läpi kutsuen tutki_ruutu-funktiota
    jokaiselle kentän sisällä olevalle alkiolle.
    """
    for i, lista in enumerate(kentta):
        for j, merkki in enumerate(lista):
            tutki_ruutu(merkki, i, j)


pelto = [
    [" ", "a", " ", " ", "l"],
    [" ", "k", "@", "k", " "],
    ["h", " ", "a", "k", " "]
]

tutki_kentta(pelto)
