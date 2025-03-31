soma = 0
for impares in range(1, 500, 2):
    print(impares)
    if impares % 3 == 0:
        print(f'O número {impares} é multiplo de 3')
        soma = soma + impares
        
print(f'A soma de todos o numeros impares multimplos de 3 é: {soma}')