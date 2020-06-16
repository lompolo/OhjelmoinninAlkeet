operator = input('Valitse operaatio (+, -, *, /): ')

if operator in ['+', '-', '*', '/']:
    try:
        luku1 = float(input('Anna luku 1: '))
        luku2 = float(input('Anna luku 2: '))
    except ValueError:
        print('Ei tämä ole mikään luku')
    else:
        if operator == '+':
            print('Tulos: {}'.format(luku1 + luku2))
        elif operator == '-':
            print('Tulos: {}'.format(luku1 - luku2))
        elif operator == '*':
            print('Tulos: {}'.format(luku1 * luku2))
        elif operator == '/':
            if luku2 == 0.0:
                print('Tällä ohjelmalla ei pääse äärettömyyteen')
            else:
                print('Tulos: {}'.format(luku1 / luku2))
else:
    print('Operaatiota ei ole olemassa')