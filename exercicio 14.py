valor_imovel = int(input('Digite o valor do imovel que deseja adquirir:'))
salario = int(input('Digite aqui o valor de seu salario:'))
qntd_prestacoes = int(input('Digite aqui a quantidade de prestações em que deseja pagar'))
valor_prestacao = valor_imovel / qntd_prestacoes

if valor_prestacao <= (salario * 0.30):
    print(f'Parabéns, seu empréstimo foi aprovado! \n'
          f'e sua parcela mensal será de {valor_prestacao:.2f}')
    
else:
    print('Infelizmente não conseguimos aprovar o empréstimo.')