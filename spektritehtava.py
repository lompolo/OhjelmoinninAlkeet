def laske_parametrit(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    b = (x2 * y1 - x1 * y2) / (x2 - x1)
    return k, b


mx1 = float(input('Anna ensimmäisen pisteen x-koordinaatti: '))
my1 = float(input('Anna ensimmäisen pisteen y-koordinaatti: '))
mx2 = float(input('Anna toisen pisteen x-koordinaatti: '))
my2 = float(input('Anna toisen pisteen y-koordinaatti: '))

if (mx1, my1) == (mx2, my2):
    print('Nämähän ovat yksi ja sama piste!')
else:
    try:
        k, b = laske_parametrit(mx1, my1, mx2, my2)
        if b < 0:
            print('Suoran yhtälö: y = {:.3f}x - {:.3f}'.format(k, -1.0*b))
        else:
            print('Suoran yhtälö: y = {:.3f}x + {:.3f}'.format(k, b))
    except ZeroDivisionError:
        print('Suora on pystysuora, yhtälöä ei voida laskea.')
