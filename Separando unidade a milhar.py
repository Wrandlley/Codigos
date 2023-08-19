num = str(input('Digite um numero: ')).strip()
nf = int(num)
print(f'Analisando numero {nf}')
if len(str(nf)) > 4:
    print('Numero invalido')
else:
    u = nf // 1 % 10
    d = nf // 10 % 10
    c = nf // 100 % 10
    m = nf // 1000 % 10
    print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''.format(u, d, c, m))