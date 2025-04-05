valores = []
for c in range(0,5):
    valores.append(int(input('Digite um valor')))
for c, v in enumerate(valores):
    print(f'O valor {v} está na posição {c}')
maior = max(valores)
menor = min(valores)
print(f'O maior valor da lista é o {maior} e está na posição {valores.index(maior)}')
print(f'O menor valor da lista é o {menor} e o menor valor é o {valores.index(menor)}')