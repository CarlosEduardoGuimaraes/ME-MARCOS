import random as r
print('O terminal mostrará um número em binário de 1 a 10, tente acertar qual número é este: ')
n = r.randint(1,10)
while True:
    print('O número em binário é: ', bin(n))
    pal = int(input('Qual o seu palpite? '))
    if pal == n:
        print('Parabéns, você acertou! O número em questão era: ', n)
        break
    else:
        print('Você errou, tente novamente')