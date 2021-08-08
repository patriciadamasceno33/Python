ficha = list()
while True:
    nome = str(input('Nome do aluno: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp in 'N':
        break
print('='*20)

print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' *30)
    opcao = int(input('Mostrar nota de qual aluno? 999 encerra: '))
    if opcao == 999:
        break
    if opcao <= len(ficha)-1:
        print(f'Notas de {ficha[opcao][0]} são: {ficha[opcao][1]}')
print('Volte Sempre')
