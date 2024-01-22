from random import randint
from time import sleep

# Inicialização de listas vazias.
lista = list()
jogos = list()

# Apresentação do título do programa.
print('-' * 15)
print('        JOGA NA DUPLA SENA        ')
print('-' * 15)

# Entrada do usuário para a quantidade de bilhetes a serem gerados.
quantidade = int(input('Quantos bilhetes quer gerar? '))
# Inicialização do contador de bilhetes gerados.
total = 1  

# Loop para gerar os bilhetes
while total <= quantidade:
    # Inicialização do contador de números únicos gerados.
    cont = 0  
    # Gera um número aleatório entre 1 e 50.
    numero = randint(1, 50)  

    # Verifica se o número gerado não está na lista.
    if numero not in lista:
        # Adiciona o número à lista.
        lista.append(numero)  
        # Incrementa o contador de números únicos.
        cont += 1  

    # Se já foram gerados 6 números únicos, encerra o loop.
    if cont >= 6:
        break

    # Ordena a lista de números.
    lista.sort()  
    # Adiciona uma cópia da lista de números ao conjunto de jogos.
    jogos.append(lista[:])  
    # Limpa a lista para gerar um novo bilhete.
    lista.clear()  
    # Incrementa o contador de bilhetes gerados.
    total += 1  

# Apresentação dos bilhetes gerados.
print('-=' * 6, f'SORTEANDO {quantidade} JOGOS ', '-=' * 6)
for i, l in enumerate(jogos):
    print(f' Jogo {i+1}: {l}')
    # Aguarda 1 segundo entre cada bilhete.
    sleep(1)  
print('-=' * 9, '< BOA SORTE!!! >', '-=' * 9)
