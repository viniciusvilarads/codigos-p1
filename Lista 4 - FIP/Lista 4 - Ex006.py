"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 4 Estrutura de Decisão
Patos - PB | 2020

6 - Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e
fazer as consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau
e o programa não deve fazer pedir os demais valores, sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes reais.
Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

"""

A = float(input("Informe o valor de A: "))
if A == 0:
    print("A não pode ter valor 0! Programa encerrado!")
else:
    B = float(input("Informe o valor de B: "))
    C = float(input("Informe o valor de C: "))

    delta = B**2 -4*A*C
    print("Delta {}".format(delta))
    if delta < 0:
        print("O delta é negativo! A equação não possui raizes reais! Encerrando programa!")
    elif delta == 0:
        raiz1 = -B / (2*A)
        raiz2 = -B / (2*A)
        print("Só possui uma raiz")
        print("Raiz {}".format(raiz1))
    else:
        raiz1 = (-B + delta**0.5) / (2*A)
        raiz2 = (-B - delta**0.5) / (2*A)
        print("Raiz 1 {}".format(raiz1))
        print("Raiz 2 {}".format(raiz2))
