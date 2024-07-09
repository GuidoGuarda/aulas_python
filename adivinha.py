import random

numero_secreto = random.randint(1, 5)

tentativas = 0

max_tentativas = 5
acertou = False

print('Bem-vindo ao Python Games!')
print(f' Você possui {max_tentativas} tentativas para advinhar o número secreto entre 1 e 5')

while tentativas < max_tentativas:
    palpite = int(input('Digite um número inteiro: '))
    tentativas +=1 

    if palpite == numero_secreto:
        acertou = True
        break
    elif palpite < numero_secreto:
        print('Tente um número maior.')
    else:
        print('Tente um número menor.')

if acertou:
    print(f'Parabéns! Você acertou o número secreto! {numero_secreto} em {tentativas} tentativas.')
else:
    print(f'Que pena! Você não conseguiu adivinhar o número secreto {numero_secreto}')
    