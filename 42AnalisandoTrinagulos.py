r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print("As retas podem formar um triângulo!")
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print("As retas não podem formar um triângulo!")
