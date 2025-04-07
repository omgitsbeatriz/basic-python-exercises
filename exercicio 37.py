lista = []
while True:
    escolha = input('Para adicionar  um número em sua lista digite A \n'
                    'Para sair da lista digite X ')
    escolha = escolha.lower()
    if escolha == 'a':
        numero = int(input('Digite o número que deseja adicionar:'))
        if numero in lista:
            print(f'Numero {numero} já se encontra na lista.')
        elif numero not in lista:
            lista.append(numero)
    elif escolha == 'x':
        print('Você saiu da lista.')
        break
    else:
        print('Digite um comando valido!')
lista.sort()
print(f'Os valores digitados foram : {lista}')
