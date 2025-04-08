lista = []
contador = 0
contador5 = 0
while True:
    escolha = input('Para adicionar um número em sua lista digite (A) \n'
                      'Para sair e conferir os valores adicionados digite (X)')
    if escolha in 'aA':
        numero = int(input('Digite o numero que deseja adicionar:'))
        lista.append(numero)
        contador += 1
        if numero == 5:
            contador5 += 1
    elif escolha in 'Xx':
        if 5 in lista:
            print(f'A sua lista em ordem decrescente é: {sorted(lista, reverse=True)} \n'
              f'foram digitados {contador} números, e o 5 foi digitado {contador5} vezes.')     
        elif 5 not in lista:
            print(f'A sua lista em ordem decrescente é: {sorted(lista, reverse=True)} \n'
              f'foram digitados {contador} números, e o 5 não foi digitado.') 
        break
    else:
        print('Digite um comando válido')