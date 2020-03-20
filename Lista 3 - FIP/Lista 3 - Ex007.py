"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 3 Estrutura de Decisão
Patos - PB | 2020

7 - Faça um Programa que leia três números e mostre o maior e o menor deles.

"""

numero1 = int(input("Informe o número 1: "))
numero2 = int(input("Informe o número 2: "))
numero3 = int(input("Informe o número 3: "))
maior = menor = 0

if (numero1 > numero2 >= numero3):
    maior = numero1
    menor = numero3
elif (numero1 > numero3 >= numero2):
    maior = numero1
    menor = numero2
elif (numero2 > numero1 >= numero3):
    maior = numero2
    menor = numero3
elif (numero2 > numero3 >= numero1):
    maior = numero2
    menor = numero1
elif (numero3 > numero1 >= numero2):
    maior = numero3
    menor = numero2
elif (numero3 > numero2 >= numero1):
    maior = numero3
    menor = numero1
else:
    print("Números iguais!")

print("Maior: {}".format(maior))
print("Menor: {}".format(menor))
