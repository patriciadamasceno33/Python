num = int(input("Digite um numero inteiro: "))
print('''Escolha uma das bases de conversao"
"[ 1 ] Converter para binários"
"[ 2 ] Converter para Octal"
"[ 3 ] Converter para decimal''')
opcao = int(input("Sua opçao: "))
if opcao == 1:
    print("Binarios: {}".format(bin(num)[2:]))
elif opcao == 2:
    print("Octal: {}".format(oct(num)[2:]))
elif opcao == 3:
    print("Decimal: {}".format(hex(num)[2:]))
else:
    print("Tente novamente")