"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1 URI
Patos - PB | 2020

A fórmula para calcular a área de uma circunferência é: 
area = π . raio2. Considerando para este problema 
que π = 3.14159:

- Efetue o cálculo da área, elevando o valor de raio ao 
quadrado e multiplicando por π.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1002

"""

raio = float(input())
area = 3.14159 * (raio**2)
print("A={:.4f}".format(area))
