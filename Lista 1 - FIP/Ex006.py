"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1
Patos - PB | 2020

6 - Escreva um programa que leia uma temperatura em graus Fahrenheit,
transforme-a em graus Celsius e exiba o resultado.

"""


fahr = float(input("Informe a temperatura em Fahrenheit: Fº"))
celsius = (fahr - 32) * (5/9)

print("{}Fº convertido para graus celsius é {:.1f}Cº".format(fahr, celsius))
