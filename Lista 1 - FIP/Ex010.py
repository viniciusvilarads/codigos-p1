"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1
Patos - PB | 2020

10 - Escreva um programa que converta valores de centímetros em polegadas.

"""


centi = float(input("Informe o valor em centímetros: "))
pol = centi / 2.54

print("{}cm em polegadas é {:.1f}pol".format(centi, pol))
