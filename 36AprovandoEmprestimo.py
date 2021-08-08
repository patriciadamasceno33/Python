casa = float(input("Qual o valor da casa a ser comprada? "))
salario = float(input("Qual o valor do seu salário? "))
anos = int(input("Em quantos anos você quer pagar a casa? "))
prestacao = casa / (anos * 12)
print("Para para uma casa de R${:.2f} em {} anos, a prestaçao será de R${:.2f}".format(casa, anos, prestacao))
if(prestacao > 0.3*salario):
    print("Empréstimo Reprovado")
else:
    print("Empréstimo Aprovado")