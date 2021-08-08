from random import randint
cont = 0
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi? ''')
computador = randint(0,10)
acertou = False
while not acertou:
    palpite = int(input('Qual o seu palpite? '))
    cont += 1
    if palpite == computador:
        acertou = True
    if palpite > computador:
        print('Menos... Tente mais uma vez')
    if palpite < computador:
        print('Mais... Tente mais uma vez')
print('O numero gerado foi {} e voce acertou com {} palpites.'.format(computador,cont))


