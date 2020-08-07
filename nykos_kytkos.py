def kysy_arvot():
    """
    Pyytää käyttäjältä liukulukuarvoja kunnes käyttäjä syöttää tyhjän. Syötetyt
    arvot palautetaan listana.
    """
    arvot = []
    
    while True:
        arvo = input("Anna vastusarvo: ")

        if not arvo:
            break

        try:
            arvo = float(arvo)
            if arvo <= 0:
                raise ValueError

            arvot.append(arvo)
        except ValueError:
            print("Komponentin arvon on oltava nollaa suurempi luku.")

    return arvot


def laske_sarja(vastukset):
    """
    Laskee annettujen vastusten kokonaisresistanssin kun ne oletetaan sarjaan
    kytketyiksi.
    """
    r_kok = 0
    for r in vastukset:
        r_kok += r
    
    return r_kok


def laske_rinnan(vastukset):
    """
    Laskee annettujen vastusten kokonaisresistanssin kun ne oletetaan rinnankytketyiksi.
    """
    r_inv = 0

    for r in vastukset:
        r_inv += r**-1
    
    return r_inv**-1


def main():
    arvot = kysy_arvot()

    if not arvot:
        print("Et antanut yhtään vastusta")
    else:
        print("Sarjaresistanssi: {}".format(laske_sarja(arvot)))
        print("Rinnakkaisresistanssi: {}".format(laske_rinnan(arvot)))


if __name__ == "__main__":
    main()
