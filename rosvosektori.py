from math import pi

def laske_sektorin_ala(sade, kulma):
    return pi * sade ** 2 * kulma / 360


r = float(input("Anna ympyrän säde: "))
alpha = float(input("Anna sektorin sisäkulma asteina: "))
print("Sektorin pinta-ala: " + str(laske_sektorin_ala(r, alpha)))