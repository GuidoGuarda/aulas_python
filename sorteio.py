import random
import os

lista = []
lista_premiados = []

while True:
    nome = input('Digite os nomes que serão sorteado: ')
    if nome != '':
        lista.append(nome)
    else:
        break

while True:
    if lista:
        os.system('cls')
        premiado = random.choice(lista)
        lista_premiados.append(premiado)
        
        print(f'O premiado foi: {premiado}')

        opcao = input('Deseja realizar um novo sorteio? (s/n): ').lower()
        os.system('cls')
      
        if opcao != 's':
            break
        
        
    else:
        print('Não existem nomes para serem sorteados!')
        break
print('Sistema finalizado.')
print(f'Participantes: {lista}')
print(f'Premiados: {lista_premiados}')        