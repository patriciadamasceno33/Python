def area(l, c):
    tam_area = l * c
    print(f'A área de um terreno {l }x {c} é de {tam_area:.2f}m²')


la = float(input('LARGURA (m): '))
co = float(input('COMPRIMENTO (m): '))
area(la, co)
