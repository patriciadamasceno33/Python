def ajuda(com):
    help(com)


#main
comando = ''
while True:
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)