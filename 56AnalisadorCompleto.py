somaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher = 0
for c in range(1, 5):
    nome = str(input('Digite o {}* nome: '.format(c)))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo M/F: '))
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher += 1
mediaidade = somaidade/4
print('A media de idade é: {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('E {} mulheres tem menos de 20 anos'.format(totalmulher))