def suodata_virhearvot(lista, reuna_arvo):
    for arvo in lista[:]:
        if arvo > reuna_arvo:
            lista.remove(arvo)


mittaukset = [12.2, 54.2, 42345.2, 23534.1, 55.7, 8982.4]
suodata_virhearvot(mittaukset, 8000)
print(mittaukset)
