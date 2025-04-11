numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
           'seis', 'sete', 'oito', 'nove', 'dez')

while True:
    n = int(input('Digite um número de 0 a 10: '))
    if 0 <= n <= 10:
        break
    print('Número inválido. Tente novamente.')

print(f'Você digitou: {numeros[n]}')
