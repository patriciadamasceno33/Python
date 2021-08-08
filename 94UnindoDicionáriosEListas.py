pessoal = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Digite M ou F ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoal.append(pessoa.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('Digite S ou N ')
    if resp == 'N':
        break
print('-'*30)
print(f'A) Quantidade de pessoas cadastradas: {len(pessoal)}')
media = soma/(len(pessoal))
print(f'B) A média de idade é: {media:5.2f}')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in pessoal:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('D) Pessoas acima da média: ', end='')
for p in pessoal:
    if p['idade'] >= media:
        print(f'{p["nome"]} ')


