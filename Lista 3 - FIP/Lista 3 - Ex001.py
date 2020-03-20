"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 3 Estrutura de Decisão
Patos - PB | 2020

1 - Faça um Programa que peça dois números e imprima o maior deles.

"""

numero1 = int(input("Informe o número 1: "))
numero2 = int(input("Informe o número 2: "))
maior = menor = 0
if numero1 > numero2:
    maior = numero1
    menor = numero2
elif numero2 > numero1:
    maior = numero2
    menor = numero1
else:
    print("Números iguais")

print("Maior; {}".format(maior))
print("Menor: {}".format(menor))
