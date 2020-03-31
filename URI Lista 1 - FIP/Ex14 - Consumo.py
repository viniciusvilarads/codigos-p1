"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1 URI
Patos - PB | 2020

Calcule o consumo médio de um automóvel sendo fornecidos a 
distância total percorrida (em Km) e o total de combustível 
gasto (em litros).

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1014

"""

X = int(input())
Y = float(input())
consumo = X / Y
print("{:.3f} km/l".format(consumo))
