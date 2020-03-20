"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 4 Estrutura de Decisão
Patos - PB | 2020

3. Faça um programa que calcule a média de consumo de combustível de um veículo.
O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km)
e quantos litros foram gastos no percurso.

"""


kmInicial = float(input("Informe o Km Inicial: "))
kmFinal = float(input("Informe o Km Final: "))
litros = float(input("Quantos litros foram gastos: "))

kmPercorrido = kmFinal - kmInicial
media = kmPercorrido / litros 

print("Foram percorridos {} Km".format(kmPercorrido))
print("Foram gastos em média {:.2f}L de combustível".format(media))

