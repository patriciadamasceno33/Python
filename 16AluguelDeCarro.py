dias = int(input("Quantos dias voce ficou com o carro? "))
km = float(input("Quantos km voce andou? "))
total = (dias * 60) + (km * 0.15)

print("O total a pagar e de: R${:.2f}".format(total))