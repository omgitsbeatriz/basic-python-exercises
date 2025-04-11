n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while True:
    print('\n[1] Somar\n[2] Multiplicar\n[3] Ver o maior\n[4] Novos números\n[5] Sair')
    operacao = int(input('Escolha a operação: '))

    if operacao == 1:
        print(f'Soma: {n1 + n2}')
    elif operacao == 2:
        print(f'Multiplicação: {n1 * n2}')
    elif operacao == 3:
        print(f'Maior: {max(n1, n2)}')
    elif operacao == 4:
        n1 = int(input('Novo valor 1: '))
        n2 = int(input('Novo valor 2: '))
    elif operacao == 5:
        print('Saindo...')
        break
    else:
        print('Opção inválida. Tente novamente.')
