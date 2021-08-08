frase = str(input("Digite uma frase: ")).lower().strip()
print("A letra A aparece {} vezes".format(frase.count('a')))
print("A primeira letra aparece na {} posicao".format(frase.find('a')))
print("A última letra aparece na {} posicao".format(frase.rfind('a')))
