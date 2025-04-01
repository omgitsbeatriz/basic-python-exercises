n = int(input('Digite o primeiro termo de uma progresão aritmética: '))
r = int(input('Digite a razão dessa progressão: '))
pa = 0
for c in range(1, 11):
    n = pa
    pa = pa + r

    print(pa, end=' ')