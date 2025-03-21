numero = int(input('Digite um numero de 0 a 9999:'))
print(numero)
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'O numero {numero} tem exatamente: \n'
      f'{u} unidades \n'
      f'{d} dezenas \n'
      f'{c} centensas \n'
      f'{m} milhares')