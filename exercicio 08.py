velocidade_carro = int(input('Digite a velocidade do seu carro:'))

if velocidade_carro >= 80:
    multa = ((velocidade_carro - 80) * 7.00)
    print(f'Seu carro foi multado em {multa} reais.')
else:
    print('Seu carro não foi multado!')
