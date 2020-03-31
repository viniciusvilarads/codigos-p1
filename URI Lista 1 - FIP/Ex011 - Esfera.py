"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1 URI
Patos - PB | 2020

Faça um programa que calcule e mostre o volume de uma esfera 
sendo fornecido o valor de seu raio (R). A fórmula para 
calcular o volume é: (4/3) * pi * R3. Considere (atribua) 
para pi o valor 3.14159.

Dica: Ao utilizar a fórmula, procure usar (4/3.0) ou (4.0/3), 
pois algumas linguagens (dentre elas o C++), assumem que o 
resultado da divisão entre dois inteiros é outro inteiro.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1011

"""

R = float(input())
VOLUME = (4/3.0) * 3.14159 * (R**3)
print("VOLUME = {:.3f}".format(VOLUME))
