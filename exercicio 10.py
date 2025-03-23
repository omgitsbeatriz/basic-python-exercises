distancia = float(input('Digite a distancia de sua vaigem:'))
tarifa1 = distancia * 0.50
tarifa2 = distancia * 0.45
if distancia <= 200:
    print(f'O preço de sua passagem é de {tarifa1} reais.')
else:
    print(f'O preço de sua passagem é de {tarifa2} reais.')