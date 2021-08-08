aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['nota'] = float(input('Média aluno: '))
print()
if aluno['nota'] <=5:
    aluno['situacao'] = 'Reprovado'
elif aluno['nota'] > 5 and aluno['nota'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Aprovado'
print('='*30)
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["nota"]}')
print(f'Situação: {aluno["situacao"]}')