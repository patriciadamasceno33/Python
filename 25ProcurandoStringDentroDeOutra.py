nome = str(input("Informe seu nome completo: ")).strip()
print("Seu nome possui Silva? {}".format('silva' in nome.lower().split()))