from math import sin, cos

def muunna_xy_koordinaateiksi(kulma, sade):
    return int(round(sade * cos(kulma), 0)), int(round(sade * sin(kulma), 0))


x, y = muunna_xy_koordinaateiksi(1.5708, 1)
print(str(x) + ", " + str(y))
