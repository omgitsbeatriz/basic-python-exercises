num1 = int(input('Digite o primeiro valor:'))
num2 = int(input('Digite o segundo valor valor:'))

if num1 > num2:
    print(f'O número {num1} é maior que o {num2}')
    
elif num2 > num1:
    print(f'O número {num2} é maior que o {num1}')
    
elif num1 == num2:
    print('Os dois números são iguais.')