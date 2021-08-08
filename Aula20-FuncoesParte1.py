def soma(*valores):
    s=0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} temos: {s}')


soma(5, 7)
soma(2, 6, 4)

'''def titulo(txt):
    print('-'*25)
    print(txt)
    print('-' * 25)

#programa principal
titulo(f'   CURSO EM VÍDEO')
titulo('    APRENDA PYTHON')'''