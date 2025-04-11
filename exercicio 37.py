lista = []

while True:
    escolha = input(
        'Para adicionar um número à lista, digite (A)\n'
        'Para sair da lista, digite (X): '
    ).strip().lower()

    if escolha == 'a':
        try:
            numero = int(input('Digite o número que deseja adicionar: '))
            if numero in lista:
                print(f'O número {numero} já está na lista.')
            else:
                lista.append(numero)
        except ValueError:
            print('Digite um número válido.')
    elif escolha == 'x':
        print('Você saiu da lista.')
        break
    else:
        print('Digite um comando válido!')

lista.sort()
print(f'\nOs valores digitados foram: {lista}')
