"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020

QuestãoLeia 3 valores de ponto flutuante e efetue o cálculo 
das raízes da equação de Bhaskara. Se não for possível 
calcular as raízes, mostre a mensagem correspondente 
“Impossivel calcular”, caso haja uma divisão por 0 ou raiz de 
numero negativo.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1036

"""


A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

if A == 0:
    print("Impossivel calcular")
else:
    delta = (B**2) - 4*A*C
    if delta < 0:
        print("Impossivel calcular")
    else:
        R1 = ((-B) + (delta)**0.5)/(2*A)
        R2 = ((-B) - (delta)**0.5)/(2*A)
        print("R1 = {:.5f}".format(R1))
        print("R2 = {:.5f}".format(R2))
