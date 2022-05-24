# Módulos
from random import randint
from time import sleep

# Lista
lista = list()

# Jogos
jogos = list()

# Título
print('-' * 60)
print('        JOGA NA DUPLA SENA        ')
print('-' * 60)

# Pergunta
quantidade = int(input('Quantos bilhetes quer gerar? '))
total = 1

# Sorteando os números
while total <= quantidade:
    cont = 0
    numero = randint(1, 50)
    if numero not in lista:
        lista.append(numero)
        cont += 1
    if cont >= 6:
        break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=' * 6, f'SORTEANDO {quantidade} JOGOS ', '-=' * 6)
for i, l in enumerate(jogos):
    print(f' Jogo {i+1}: {l}')
    sleep(1)
print('-=' * 9, '< BOA SORTE!!! >', '-=' * 9)
