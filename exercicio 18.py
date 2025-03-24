ano_nasc = int(input('Digite seu ano de nascimento:'))
ano_atual = 2025
idade = ano_atual - ano_nasc

if idade < 9:
    print(f'Você tem {idade} anos e foi selecionado(a) na categoria MIRIM.')
    
elif idade > 9 and idade < 14: 
    print(f'Você tem {idade}  anos e foi selecionado(a) na categoria INFANTIL.')
    
elif idade > 14 and idade < 19:
    print(f'Você tem {idade}  anos e foi selecionado(a) na categoria JUNIOR.')

elif idade > 19 and idade < 20:
    print(f'Você tem {idade} anos e foi selecionado(a) na categoria SENIOR.')

elif idade > 20:
    print(f'Você tem {idade} anos e foi selecionado(a) na categoria MASTER.')