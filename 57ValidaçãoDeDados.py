sexo = str(input('Digite o sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, digite o sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
