vel = float(input("Qual a velocidade do seu carro? "))
if vel <= 80:
    print("Dentro do limite. Dirija com cuidado.")
else:
    vel = vel - 80
    print("Você está acima da velocidade! Vai pagar uma multa de {}.".format(vel*7))
