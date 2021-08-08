tupla = ('abajur', 'mouse', 'tesoura', 'ventilador', 'armario', 'rede', 'cama', 'espelho')
for t in tupla:
    print(f'\nA palavra {t} tem as vogais: ', end='')
    for letra in t:
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end='')
