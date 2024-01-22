from random import randint
from time import sleep

# Inicialização de listas vazias
lista = list()
jogos = list()

# Apresentação do título do programa
print('-' * 15)
print('        JOGA NA DUPLA SENA        ')
print('-' * 15)

# Entrada do usuário para a quantidade de bilhetes a serem gerados
quantidade = int(input('Quantos bilhetes quer gerar? '))
total = 1  # Inicialização do contador de bilhetes gerados

# Loop para gerar os bilhetes
while total <= quantidade:
    cont = 0  # Inicialização do contador de números únicos gerados
    numero = randint(1, 50)  # Gera um número aleatório entre 1 e 50

    # Verifica se o número gerado não está na lista
    if numero not in lista:
        lista.append(numero)  # Adiciona o número à lista
        cont += 1  # Incrementa o contador de números únicos

    # Se já foram gerados 6 números únicos, encerra o loop
    if cont >= 6:
        break

    lista.sort()  # Ordena a lista de números
    jogos.append(lista[:])  # Adiciona uma cópia da lista de números ao conjunto de jogos
    lista.clear()  # Limpa a lista para gerar um novo bilhete
    total += 1  # Incrementa o contador de bilhetes gerados

# Apresentação dos bilhetes gerados
print('-=' * 6, f'SORTEANDO {quantidade} JOGOS ', '-=' * 6)
for i, l in enumerate(jogos):
    print(f' Jogo {i+1}: {l}')
    sleep(1)  # Aguarda 1 segundo entre cada bilhete
print('-=' * 9, '< BOA SORTE!!! >', '-=' * 9)

from random import randint
from time import sleep


lista = list()


jogos = list()


print('-' * 15)
print('        JOGA NA DUPLA SENA        ')
print('-' * 15)


quantidade = int(input('Quantos bilhetes quer gerar? '))
total = 1

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
