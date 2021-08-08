d = float(input("Forneça a distancia da viagem em Km: "))
if d <= 200:
    preco = d*0.5
    print("O valor da viagem será: R${:.2f}".format(preco))
else:
    preco = d*0.45
    print("O valor da viagem será: R${:.2f}".format(preco))

#preco = d*0.5 if d<=200 else d*0.45