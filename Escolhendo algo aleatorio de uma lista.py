import random
p = str(input('Primeiro candidato: '))
pp = str(input('Segundo candidato: '))
ppp = str(input('Terceiro candidato: '))
pppp = str(input('Quarto candidato: '))
lista = [p, pp, ppp, pppp]
print(f'O candidato escolhido para apagar o quadro foi {random.choice(lista)}')