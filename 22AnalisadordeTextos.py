nome = input(print("Informe seu nome completo")).strip()
print("Seu nome maiúsculo é: {}".format(nome.upper()))
print("Seu nome minúsculo é: {}".format(nome.lower()))
print("Quantidade de letras: {}".format(len(nome)-nome.count(' ')))
print("O primeiro nome tem: {} letras".format(nome.find(' ')))
#outra forma de contar o primeiro nome
separa = nome.split()
print("O primeiro nome tem: {} letras".format(len(separa[0])))