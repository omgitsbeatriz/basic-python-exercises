lista = []
contador = 0
contador5 = 0

while True:
    escolha = input(
        'Para adicionar um número na lista, digite (A)\n'
        'Para sair e conferir os valores, digite (X): '
    ).strip().upper()

    if escolha == 'A':
        numero = int(input('Digite o número que deseja adicionar: '))
        lista.append(numero)
        contador += 1
        if numero == 5:
            contador5 += 1
    elif escolha == 'X':
        lista_ordenada = sorted(lista, reverse=True)
        print(f'\nA sua lista em ordem decrescente é: {lista_ordenada}')
        print(f'Foram digitados {contador} números.')
        if contador5 > 0:
            print(f'O número 5 foi digitado {contador5} vezes.')
        else:
            print('O número 5 não foi digitado.')
        break
    else:
        print('Comando inválido. Tente novamente.')
