t18 = s = m20 = 0
while True:
    idade = int(input('Forneça a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Forneça o sexo: [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        t18 += 1
    if sexo == 'M':
        s += 1
    if sexo == 'F' and idade < 20:
        m20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{t18} pessoas tem mais de 18 anos.')
print(f'{s} homens foram cadastrados.')
print(f'{m20} mulheres tem menos de 20 anos.')
