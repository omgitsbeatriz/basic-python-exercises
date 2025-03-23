salario = int(input('Digite seu salario e verifique seu aumento:'))
aumento1 = salario * 1.10
aumento2 = salario * 1.15

if salario >= 1250:
    print(f'Seu aumento foi 10% e seu novo salario é: {aumento1:.2f}')
else:
    print(f'Seu aumento foi 15% e seu novo salario é: {aumento2:.2f}')