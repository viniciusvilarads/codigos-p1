"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 3 Estrutura de Decisão
Patos - PB | 2020

2 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo
ou negativo.

"""

numero = int(input("Número: "))
validade = ""

if numero > 0:
    validade = "positivo"
elif numero < 0:
    validade = "negativo"
else:
    validade = "nulo"

print("Valor {}".format(validade))
