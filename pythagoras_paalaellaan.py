from math import sqrt


def laske_sivun_pituus(hypotenuusa):
    return sqrt(1 / 2 * hypotenuusa ** 2)


h = float(input("Anna tasakylkisen kolmion hypotenuusan pituus: "))
print("Kylkien pituus: " + str(laske_sivun_pituus(h)))
