def laske_parametrit(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    b = (x2 * y1 - x1 * y2) / (x2 - x1)
    return k, b

def kysy_kaksi_lukua(merkkijono):
    """
    Pyytää käyttäjältä kaksi liukulukua välilyönnillä erotettuna. Syötettä kysytään
    kunnes käyttäjä antaa kaksi kelvollista liukulukua. Syötetyt luvut palautetaan
    liukulukuina.
    """
    while True:
        syote = input(merkkijono).split(" ")

        if len(syote) != 2:
            print("Anna kaksi lukua välilyönnillä erotettuna")
            continue

        try:
            x = float(syote[0])
            y = float(syote[1])
            break
        except:
            print("Anna kaksi lukua välilyönnillä erotettuna")

    return x, y


def laske_pisteet_suoralla(k, b, x_pisteet):
    """
    Tuottaa joukon arvoja, jotka ovat annetulla kulmakertoimella ja vakiotermillä
    määritetyn suoran arvoja annetuissa x-akselin pisteissä.
    """
    
    return [k*x + b for x in x_pisteet]


def main():
    x_akseli = [
        0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5,
        2.75, 3.0, 3.25, 3.5, 3.75, 4.0, 4.25, 4.5, 4.75, 5.0
    ]
    print("main")
    x1, y1 = kysy_kaksi_lukua("Anna ensimmäinen piste: ")
    x2, y2 = kysy_kaksi_lukua("Anna toinen piste: ")

    k, b = laske_parametrit(x1, y1, x2, y2)

    for y in laske_pisteet_suoralla(k, b, x_akseli):
        print("{:.4f}".format(y), end=" ")


if __name__ == "__main__":
    main()