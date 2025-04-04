while True:
    numero = int(input('Digite o número para ver a tabuada: \n'
                       '(Não é possivel verificar números negativos)'))
    if numero < 0:
        break
    for n in range(1,11):
        print(f'{numero} x {n} = {numero * n}')
print('Tabuada encerrada!')