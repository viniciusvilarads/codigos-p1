A, B, C = input().split()
"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1 URI
Patos - PB | 2020

Escreva um programa que leia três valores com ponto flutuante 
de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B. 

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1012

"""

A = float(A)
B = float(B)
C = float(C)
TRIANGULO = (A * C)/2
CIRCULO = 3.14159 * (C**2)
TRAPEZIO = ((A + B) * C) / 2
QUADRADO = B * B
RETANGULO = A * B
print("TRIANGULO: {:.3f}".format(TRIANGULO))
print("CIRCULO: {:.3f}".format(CIRCULO))
print("TRAPEZIO: {:.3f}".format(TRAPEZIO))
print("QUADRADO: {:.3f}".format(QUADRADO))
print("RETANGULO: {:.3f}".format(RETANGULO))
