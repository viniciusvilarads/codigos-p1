"""
3. Faça um programa que calcule a média de consumo de combustível de um veículo.
O usuário deve informar o KM inicial (ex. 12500 km), o KM final (ex. 12700 km)
e quantos litros foram gastos no percurso.

**CONSIDERANDO QUE O CARRO FAZ 1L POR 15KM
"""

kmInicial = float(input("Informe o Km Inicial: "))
kmFinal = float(input("Informe o Km Final: "))
litros = float(input("Quantos litros foram gastos: "))

media = litros / (kmFinal - kmInicial)

print("Foram gastos em média {:.2f}L de combustível".format(media))

