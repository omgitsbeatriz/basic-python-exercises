cidade = input('Digite sua cidade')
c = cidade.find('santo'.lower())
if c == 0:
    print('A cidade começa com Santo.')
else:
    print('A cidade não começa com santo')