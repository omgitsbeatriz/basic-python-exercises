ano_nascimento = int(input('Digite seu ano de nascimento:'))
ano_atual = 2025
idade = ano_atual - ano_nascimento

if idade == 18:
    print(f'Você tem {idade} deve se alistar no exécito.')
    
elif idade < 18:
    print('Você tem {idade} anos e está proximo de se alistar.')
    
elif idade > 18:
    print(f'Você tem {idade} anos, e já passou da hora de se alistar.')