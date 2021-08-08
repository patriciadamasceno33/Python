from datetime import date
atual = date.today().year
nascimento = int(input("Em qual ano voce nasceu? "))
idade = atual - nascimento
print("Quem nasceu em {} tem {} anos em {}".format(nascimento, idade, atual))
if idade < 18:
    print("Ainda faltam {} anos para o alistamento".format(18 - idade))
    print("Seu alistamento será em {}".format(nascimento+18))
elif idade > 18:
    print("Voce ja deveria ter se alistado ha {} anos".format(idade-18))
    print("Seu alistamento foi em {}".format(nascimento+18))
else:
    print("Voce tem que se alistar imediatamente")

