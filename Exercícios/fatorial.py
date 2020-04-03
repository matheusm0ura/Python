n = int(input('Digite um número: '))
c = n
fat = 1
print('{}! ='.format(n), end= ' ')
while c > 0:
    print('{}'.format(c), end= '')
    print(' x ' if c > 0 else ' = ', end= '')
    fat *= c
    c -= 1
print(fat)
