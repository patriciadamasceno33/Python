sal = float(input("Qual o valor do seu salário? "))
if sal <= 1250:
    sal = sal + (sal * 0.15)
else:
    sal = sal + (sal * 0.10)
print("Agora o seu salário é: {}".format(sal))
