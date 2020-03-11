"""
7. Faça um programa que calcule a área total (m​2​) de uma casa com 4 cômodos.
O usuário deve inserir a largura e comprimento de cada um dos cômodos,
calcular a área individual de cada um e por fim exibir a área total da casa.
"""

largPrimComodo = float(input("Largura 1º cômodo: "))
compPrimComodo = float(input("Comprimento 1º cômodo: "))

largSegComodo = float(input("Largura 2º cômodo: "))
compSegComodo = float(input("Comprimento 2º cômodo: "))

largTerComodo = float(input("Largura 3º cômodo: "))
compTerComodo = float(input("Comprimento 3º cômodo: "))

largQuaComodo = float(input("Largura 4º cômodo: "))
compQuaComodo = float(input("Comprimento 4º cômodo: "))

primComodo = largPrimComodo * compPrimComodo
segComodo = largSegComodo * compSegComodo
terComodo = largTerComodo * compTerComodo
quaComodo = largQuaComodo * compQuaComodo

largTotal = largPrimComodo + largSegComodo + largTerComodo + largQuaComodo
compTotal = compPrimComodo + compSegComodo + compTerComodo + compQuaComodo

areaTotal = largTotal * compTotal

print("Área do primeiro cômodo {:.2f}m^2".format(primComodo))
print("Área do segundo cômodo {:.2f}m^2".format(segComodo))
print("Área do terceiro cômodo {:.2f}m^2".format(terComodo))
print("Área do quarto cômodo {:.2f}m^2".format(quaComodo))

print("Área total {:.2f}m^2".format(areaTotal))
