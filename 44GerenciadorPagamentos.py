preco = float(input('Forneça o preço das compras!'))
fdp = int (input('''FORMAS DE PAGAMENTO
[1] À VISTA DINHEIRO/CHEQUE
[2] À VISTA NO CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO
Escolha uma das opções: '''))
if fdp == 1:
    preco = preco - (preco*0.10)
    print('Voce pagará R${}'.format(preco))
elif fdp == 2:
    preco = preco - (preco * 0.05)
    print('Voce pagará R${}'.format(preco))
elif fdp == 3:
    preco = preco/2
    print('Voce pagará duas parcelas de R${}'.format(preco))
elif fdp == 4:
    parcelas = int(input('Quantas parcelas? '))
    preco = preco + (preco * 0.2)
    pagar = preco/parcelas
    print('Voce pagará {} parcelas de R${}'.format(parcelas, pagar))
    print('O valor final da sua compra será de R${}'.format(preco))
else:
    print("Opção Inválida!")