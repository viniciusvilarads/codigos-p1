"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 4 Estrutura de Decisão
Patos - PB | 2020

5 - Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem
um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
- Três lados formam um triângulo quando a soma de quaisquer dois lados for maior
que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;

"""

lado1 = float(input("Informe o lado 1: "))
lado2 = float(input("Informe o lado 2: "))
lado3 = float(input("Informe o lado 3: "))

if ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado2 + lado3) > lado1):
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero")
    elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
        print("Triângulo Isóceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não e triângulo")
