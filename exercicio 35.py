a = int(input('Digite o 1º valor: '))
b = int(input('Digite o 2º valor: '))
c = int(input('Digite o 3º valor: '))
d = int(input('Digite o 4º valor: '))
e = int(input('Digite o 5º valor: '))

tupla = (a, b, c, d, e)

contador9 = tupla.count(9)
print(f'O valor 9 apareceu {contador9} vezes.')

if 3 in tupla:
    posicao3 = tupla.index(3)
    print(f'O valor 3 apareceu pela primeira vez na {posicao3 + 1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
