numeros = []
for c in range(0,5):
    num = int(input('Digite um valor:'))
    if c == 0:
        print('Adicionado na última posição')
        numeros.append(num)
    else:
        if num < numeros[0]:
            print('Adicionado na posição 0.')
            numeros.insert(0, num)
        elif num > numeros[-1]:
            print('Adicionado na última posição.')
            numeros.append(num)
        elif numeros[0] < num <= numeros[1]:
            print('Adicionado na posição 1.')
            numeros.insert(1, num)
        elif numeros[1] < num <= numeros[2]:
            print('Adicionado na posição 2.')
            numeros.insert(2, num)
        elif numeros[2] < num <= numeros[3]:
            print('Adicionado na posição 3.')
            numeros.insert(3, num)
print(numeros)