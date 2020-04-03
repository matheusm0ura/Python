a1 = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
t = a1
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{} -* '.format(t), end= '')
        t += r
        c += 1
    print('PAUSA')
    mais = int(input('Digite quantos termos você quer a mais: '))
print('P.A finalizada com {} termos'.format(total))
