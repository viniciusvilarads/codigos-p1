"""
9. Escreva um programa que converte valores de polegadas em centímetros
utilizando a seguinte fórmula para conversão: 1 polegada = 2,54 cm;
"""

pol = float(input("Informe o valor em polegadas: "))
cent = pol * 2.54

print("{}pol é igual a {:.2f}cm".format(pol, cent))
