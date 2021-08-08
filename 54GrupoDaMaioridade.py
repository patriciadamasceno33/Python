from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input('Em que ano a {}* pessoa nasceu? '.format(c)))
    if atual - nascimento >= 18:
        maior += 1
    elif atual - nascimento < 18:
        menor += 1
print('\nTivemos {} pessoas maior de idade e {} menor de idade'.format(maior, menor))