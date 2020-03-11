"""
4. Escreva um programa que leia uma temperatura em graus Fahrenheit,
transforme-a em graus Celsius e exiba o resultado.
"""

fahr = float(input("Grau Fahrenheit: "))

celsius = (fahr - 32) * (5/9)

print("{}ªF para ªC é {:.1f}ªC".format(fahr, celsius))

