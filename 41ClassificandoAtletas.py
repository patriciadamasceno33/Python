from datetime import date
ano = int(input('Qual o seu ano de nascimento? '))
idade = date.today().year - ano
if idade <= 9:
    classificacao = 'MIRIM'
elif idade >= 10 and idade <= 14:
    classificacao = 'INFANTIL'
elif idade >= 15 and idade <= 19:
    classificacao = 'JUNIOR'
elif idade >= 20 and idade <= 25:
    classificacao = 'SENIOR'
elif idade >= 25:
    classificacao = 'MASTER'
else:
    classificacao = 'OPÇAO INVÁLIDA'
print('''O atleta tem {} anos.
Classificaçao: {}'''.format(idade, classificacao))
