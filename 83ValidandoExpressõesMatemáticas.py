ex = str(input('Digite e expressão: '))
p = []
for sim in ex:
    if sim == '(':
        p.append('(')
    elif sim == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Sua expressão está certa!')
else:
    print('Sua expressão está errada!')