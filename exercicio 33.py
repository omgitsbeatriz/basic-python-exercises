numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez' )

while True:
    n = int(input('Digite numero de 0 a 10: '))
    if n > 10 or n < 0:
        n = int(input('Digite numero de 0 a 10: '))
    break

print(f"voce digitou: {numeros[n]}")
