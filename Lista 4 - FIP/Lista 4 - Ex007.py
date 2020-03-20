"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 4 Estrutura de Decisão
Patos - PB | 2020

7 - Faça um Programa que peça um número correspondente a um determinado ano e
em seguida informe se este ano é ou não bissexto.
"""

ano = int(input("Informe o ano: "))
if (ano%4 == 0 and ano%100 != 0) or (ano%400 == 0):
    print("Ano Bissexto!")
else:
    print("Ano não bissexto!")
