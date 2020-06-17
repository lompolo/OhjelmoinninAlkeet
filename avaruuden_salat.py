import math

def laske_pituus(janan_pisteet):
    delta_x = abs(janan_pisteet[0] - janan_pisteet[2])
    delta_y = abs(janan_pisteet[1] - janan_pisteet[3])
    return math.sqrt(delta_x ** 2 + delta_y ** 2)


pituus = laske_pituus([1, 1, 2, 1])
print(pituus)
