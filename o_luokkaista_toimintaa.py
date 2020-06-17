def laske_ninjat(x, y, lista):
    korkeus = len(lista)
    leveys = len(lista[0])

    if x < 0 or x >= leveys or y < 0 or y >= korkeus:
        return 0

    if y < 1:
        y_lista = lista[0:2]
    elif  y > korkeus - 1:
        y_lista = lista[y-1:korkeus]
    else:
        y_lista = lista[y-1:y+2]

    if x - 1 < 0:
        x_start = 0
    else:
        x_start = x - 1

    ninja_count = 0

    for x_lista in y_lista:
        for j, merkki in enumerate(x_lista):
            if j < x_start:
                continue
            if j >= x + 2:
                break
            if merkki == 'N':
                ninja_count += 1
        
    return ninja_count


huone = [['N', ' ', ' ', ' ', ' '],
         ['N', 'N', 'N', 'N', ' '],
         ['N', ' ', 'N', ' ', ' '],
         ['N', 'N', 'N', ' ', ' '],
         [' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ']]

print(laske_ninjat(0, 0, huone))
print(laske_ninjat(4, 5, huone))
print(laske_ninjat(3, 3, huone))
print(laske_ninjat(1, 2, huone))
