times = ('Fortaleza', 'Juventude', 'Vasco da Gama', 'Cruzeiro', 'Grêmio', 'Bragantino',
             'Ceará', 'Corinthians', 'Flamengo', 'Internacional', 'Bahia', 'São Paulo', 'Sport',
             'Botafogo', 'Palmeiras','Atlético', 'Santos', 'Mirassol', 'Fluminense', 'Vitória')

print(f'Os 5 primeiro colocados são: {times[0:5]}')
print(f'Os quatro ultimos colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética: {sorted(times)}')

time = input('Qual time deseja verificar a posição?')
posição = times.index(time)
print(f'{time} está na {posição + 1 }º posição.')