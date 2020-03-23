"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1
Patos - PB | 2020

9 - Escreva um programa que converte valores de polegadas em centímetros
utilizando a seguinte fórmula: 1 polegada = 2,54cm;

"""


pol = float(input("Informe o valor em polegadas: "))
centi = pol * 2.54

print("{}pol em centímetros é {:.2f}cm".format(pol, centi))
