dados= {}
dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] == 0:
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratação'] + 35) - dados['nascimento']
    for k, v in dados.items():
        print(f'- {k} tem o valor {v}')