import random

n_aleatorio = random.randint(0,5)
guessuser = int(input('Adivinhe o numero:'))

if guessuser == n_aleatorio:
    print(f'Prabens você acertou, o numero aleatorio é: {n_aleatorio}!')
else:
    print('Não foi dessa vez! :(')