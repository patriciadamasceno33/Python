peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)
print('Seu IMC é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do Peso')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal')
elif 25 <= imc < 30:
    print("Você está com sobrepeso")
elif 30 <= imc < 40:
    print('Você está obeso')
elif imc >= 40:
    print('Você está com obesidade mórbida')
