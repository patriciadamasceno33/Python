try:
    a = int(input('Numerador:'))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com o tipo de dado informado')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os valores')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Muito obrigada! Volte sempre.')