a = input('Digite o 1º valor:')
b = input('Digite o 2º valor:')
c = input('Digite o 3º valor:')
d = input('Digite o 4º valor:')
e = input('Digite o 5º valor:')
tupla = (a, b, c, d, e)
contador9 = tupla.count('9')
print(f'O valor 9 apareceu {contador9} vezes')
if '3' not in tupla:
    print('O valor 3 não foi digitado.')
else:
    posição3 = tupla.index('3')
    print(f'O valor 3 aparece a primeira vez na {posição3 + 1}º posição.')
