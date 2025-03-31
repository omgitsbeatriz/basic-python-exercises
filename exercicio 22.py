import random

jogada_pc = random.randint(0,10)
jogada_usuario = int(input('Adivinhe o numero:'))
contador = 1

while jogada_usuario != jogada_pc:
    jogada_usuario = int(input('Você errou, tente novamente..'))
    contador += 1
print(f'você acertou, foram {contador} palpites até você digitar {jogada_usuario} e o computador {jogada_pc}')