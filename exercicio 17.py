nota1 = float(input('Digite a sua primira  nota:'))
nota2 = float(input('Digite a sua segunda nota:'))

media = (nota1 + nota2) / 2

if media > 7.0:
    print(f'Você obteve nota {media:.2f}, e está aprovado. Prabéns!')
    
elif media > 5.0 and media < 6.9:
    print(f'Você obteve nota {media:.2f}, e está de recuperação.')
    
elif media < 5.0:
    print(f'Você obteve nota {media:.2f}, e está reprovado.')