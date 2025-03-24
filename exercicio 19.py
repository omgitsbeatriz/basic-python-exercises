preco_produto = float(input('Digite o valor do produto:'))
forma_pgto = str(input('dogite a forma de pagamento (dinheiro, cheque ou cartão)'))
qntd_parcelas = float(input('Digite a quantidade de parcelas:'))

if forma_pgto == 'dinheiro' or forma_pgto == 'cheque':
    print(f'O valor do produto com desconto será de {preco_produto * 0.90:.2f}')
    
elif forma_pgto == 'cartão':
    if qntd_parcelas == 1:
        print(f'O valor do produto com desconto será de {preco_produto * 0.95:.2f}')
    
    elif qntd_parcelas == 2:
        print(f'O valor do produto não teve alteração e será de {preco_produto}')
        
    elif qntd_parcelas > 3:
        print(f'O valor do produto com juros será de {preco_produto * 1.20:.2f}')