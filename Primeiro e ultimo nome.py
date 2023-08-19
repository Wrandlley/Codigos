name = str(input('Digite seu nome completo: ')).title().strip()
n = name.split()
print('Olá, {} {}. Seja bem vindo!'.format(n[0], n[len(n)-1]))
