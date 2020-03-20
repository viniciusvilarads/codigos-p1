"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 3 Estrutura de Decisão
Patos - PB | 2020

8 - Faça um programa que pergunte o preço de três produtos e informe qual
produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

"""

prod1 = float(input("Informe o preço do produto 1: "))
prod2 = float(input("Informe o preço do produto 2: "))
prod3 = float(input("Informe o preço do produto 3: "))
menor = 0

if (prod1 > prod2 >= prod3):
    menor = prod3
elif (prod1 > prod3 >= prod2):
    menor = prod2
elif (prod2 > prod1 >= prod3):
    menor = prod3
elif (prod2 > prod3 >= prod1):
    menor = prod1
elif (prod3 > prod1 >= prod2):
    menor = prod2
elif (prod3 > prod2 >= prod1):
    menor = prod1
else:
    print("Preços iguais!")

print("Melhor produto custa: R${:.2f}".format(menor))
