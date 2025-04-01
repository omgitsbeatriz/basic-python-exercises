soma = 0

for ni in range(0,6):
    n1 = int(input('Digite um numero aleatorio:'))
    if n1 % 2 != 0:
        soma = soma + n1
print(f'A soma dos números impares digitados é: {soma}')