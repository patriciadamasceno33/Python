from random import randint
from time import sleep
comp = randint(0,5)
jog = int(input("Vou pensar em um numero entre 0 e 5. Tente adivinhar "))
print("PROCESSANDO")
sleep(2)
if comp == jog:
    print("Você Acertou, o numero é {}! Parabéns".format(comp))
else:
    print("Voce errou, o numero é {}. Tente novamente".format(comp))
