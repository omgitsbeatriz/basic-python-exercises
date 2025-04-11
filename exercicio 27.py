soma = 0

for i in range(6):
    n = int(input('Digite um número aleatório: '))
    if n % 2 != 0:
        soma += n

print(f'\nA soma dos números ímpares digitados é: {soma}')
