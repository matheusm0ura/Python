n = int(input('Digite quantos termos você quer na sua seqência de Fibonacci: '))
while n == 0:
    n = int(input('Digite quantos termos você quer na sua seqência de Fibonacci: '))
if n == 1 or n == 2:
    print('1', end='')
else:
    t1 = 0
    t2 = 1
    print('{} → {}'.format(t1, t2), end='')
    c = 3
    while c <= n:
        t3 = t1 + t2
        print(' → {}'.format(t3), end='')
        t1 = t2
        t2 = t3
        c += 1
print(' → FIM')
