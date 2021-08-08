from math import sin, cos, tan, radians
ang = float(input("Digite o angulo que voce deseja: "))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print("Seno: {:.2}, Cosseno: {:.2} e Tangente {:.2}".format(seno, cos, tan))