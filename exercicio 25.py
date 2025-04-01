n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o segundo valor:'))
opcao = 0
print('Escolha a operação que deseja realizar: \n'
      '[1] Somar \n'
      '[2] Multiplicar \n'
      '[3] Ver o maior \n'
      '[4] Novos números \n'
      '[5] Sair')

escolha = (1, 2, 3, 4, 5)
while opcao == 0:
     opcao = int(input('Digite uma Opção: '))   

if opcao == 1:
        print(f'A soma de {n1} + {n2} = {n1 + n2}.')
elif opcao == 2:
        print(f'A multiplicação de {n1} x {n2} = {n1 * n2}')
elif opcao == 3:
        print(f'O maior numero entre {n1} e {n2} é {max(n1, n2)}')
elif opcao == 4:
        n1 = int(input('Digite o primeiro valor:'))
        n2 = int(input('Digite o segundo valor:'))
elif opcao == 5:
    print('Fim')