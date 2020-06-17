def pyyda_syote(pyynto, virhe):
    """
    Kysyy käyttäjältä kokonaislukua käyttäen kysymyksenä parametrina annettua
    merkkijonoa. Virheellisen syötteen kohdalla käyttäjälle näytetään toisena
    parametrina annettu virheilmoitus. Käyttäjän antama kelvollinen syöte
    palautetaan kokonaislukuna. Hyväksyy vain luvut jotka ovat suurempia kuin 1.
    """
    while True:
        try:
            luku = int(input(pyynto))
        except ValueError:
            print(virhe)
        else:
            if luku < 2:
                print(virhe)
            else:
                return luku


def tarkista_alkuluku(luku):
    """
    Tarkistaa onko parametrina annettu luku alkuluku. Palauttaa False jos luku ei
    ole alkuluku; jos luku on alkuluku palautetaan True
    """
    for i in range(2, luku//2 + 1):
        if luku % i == 0:
            return False
    return True


luku = pyyda_syote(
    "Anna kokonaisluku, joka on suurempi kuin 1: ",
    "Pieleen meni :'(."
)

if tarkista_alkuluku(luku):
    print('Kyseessä on alkuluku.')
else:
    print('Kyseessä ei ole alkuluku.')