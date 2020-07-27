import haravasto

field = []

def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    haravasto.tyhjaa_ikkuna()
    haravasto.piirra_tausta()
    haravasto.aloita_ruutujen_piirto()
    
    for y, lista in enumerate(field):
        for x, merkki in enumerate(lista):
            haravasto.lisaa_piirrettava_ruutu(merkki, x*40, y*40)

    haravasto.piirra_ruudut()

def tarkista(kentta, x, y):
    if x < 0 or y < 0 or x >= len(kentta[0]) or y >= len(kentta):
        return False
    if kentta[y][x] == "x" or kentta[y][x] == "0":
        return False
    return True

def tulvataytto(kentta, x, y):
    """
    Merkitsee planeetalla olevat tuntemattomat alueet turvalliseksi siten, että
    täyttö aloitetaan annetusta x, y -pisteestä.
    """
    if not tarkista(kentta, x, y):
        return
    
    queue = []
    queue.append((x,y))

    while len(queue) > 0:
        x, y = queue.pop()
        if tarkista(kentta, x, y):
            kentta[y][x] = "0"

        if tarkista(kentta, x+1, y):
            queue.append((x+1, y))
        if tarkista(kentta, x+1, y-1):
            queue.append((x+1, y-1))
        if tarkista(kentta, x, y-1):
            queue.append((x, y-1))
        if tarkista(kentta, x-1, y-1):
            queue.append((x-1, y-1))
        if tarkista(kentta, x-1, y):
            queue.append((x-1, y))
        if tarkista(kentta, x-1, y+1):
            queue.append((x-1, y+1))
        if tarkista(kentta, x,y+1):
            queue.append((x, y+1))
        if tarkista(kentta, x+1, y+1):
            queue.append((x, y+1))



def main(planeetta):
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen piirtokäsittelijän.
    """
    global field
    field = planeetta

    print(field)
    haravasto.lataa_kuvat("c:/Projektit/Python/OhjelmoinninAlkeet/OhjelmoinninAlkeet/spritet")
    haravasto.luo_ikkuna(len(planeetta[0]*40), len(planeetta*40))
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aloita()


if __name__ == "__main__":
    planeetta = [
        [" ", " ", " ", "x", " ", " ", " ", " ", " ", " ", " ", "x", " "], 
        [" ", " ", "x", "x", " ", " ", " ", "x", " ", " ", " ", "x", " "], 
        [" ", "x", "x", " ", " ", " ", " ", "x", " ", " ", "x", "x", " "], 
        ["x", "x", "x", "x", "x", " ", " ", "x", " ", "x", " ", " ", " "], 
        ["x", "x", "x", "x", " ", " ", " ", " ", "x", " ", "x", " ", " "], 
        [" ", " ", "x", " ", " ", " ", " ", " ", " ", "x", " ", " ", " "]
    ]

    tulvataytto(planeetta, 6, 5)
    main(planeetta)