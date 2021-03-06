"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020



Leia 3 valores de ponto flutuante A, B e C e ordene-os em 
ordem decrescente, de modo que o lado A representa o maior 
dos 3 lados. A seguir, determine o tipo de triângulo que estes 
três lados formam, com base nos seguintes casos, sempre 
escrevendo uma mensagem adequada:

    se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
    se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1045

"""

N1, N2, N3 = input().split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)

valores = list()
valores.append(N1)
valores.append(N2)
valores.append(N3)

A = max(valores)
valores.remove(max(valores))
B = max(valores)
valores.remove(max(valores))
C = max(valores)
valores.remove(max(valores))

if A >= (B+C):
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif (A == B) or (A == C) or (B==C):
        print("TRIANGULO ISOSCELES")
