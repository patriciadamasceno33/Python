n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
print('A media é: {}'.format(media))
if media < 6:
    print('Voce foi reprovado')
elif media >= 5.0 or media <= 6.9:
    print('Voce esta em recuperacao')
elif media >= 7:
    print('Voce foi Aprovado')
