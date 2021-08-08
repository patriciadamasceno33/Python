from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f'Com {idade} anos: NÃO VOTA!')
    elif 16 <= idade < 18 or idade > 65:
        print(f'Com {idade} anos: OPCIONAL!')
    else:
        print(f'Com {idade} anos: OBRIGATÓRIO!')

nas = int(input('Qual o seu ano de nascimento? '))
voto(nas)
