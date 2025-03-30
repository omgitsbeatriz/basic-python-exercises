import random
from time import sleep

jogada_user = input('Digite a sua jogada:')
l = ['pedra', 'papel', 'tesoura']
jogada_pc = random.choice(l)

from time import sleep
print('JO', end='')
sleep(0.6)
print('KEN', end='')
sleep(0.6)
print('PO!!!')
sleep(0.1)

print(f'O usuario jogou {jogada_user}, e o computador jogou {jogada_pc}')

if jogada_user == 'tesoura' and jogada_pc == 'tesoura':
    print('Os dois joagaram a mesma coisa então deu empate!')
elif jogada_user == 'papel' and jogada_pc == 'papel':
    print('Os dois joagaram a mesma coisa então deu empate!')
elif jogada_user == 'pedra' and jogada_pc == 'pedra':
    print('Os dois joagaram a mesma coisa então deu empate!')
    
elif jogada_user == 'papel' and jogada_pc == 'pedra':
    print('O usuario ganhou!')
elif jogada_user == 'pedra' and jogada_pc == 'tesoura':
    print('O usuario ganhou!')
elif jogada_user == 'tesoura' and jogada_pc == 'papel':
    print('O usuario ganhou!')
elif jogada_pc == 'papel' and jogada_user == 'pedra':
    print('O computador ganhou!')   
elif jogada_pc == 'pedra' and jogada_user == 'tesoura':
    print('O computador ganhou!') 
elif jogada_pc == 'tesoura' and jogada_user == 'papel':
    print('O computador ganhou!')
       
else:
    print('digite uma jogada válida!')