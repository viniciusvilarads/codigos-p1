"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 4 Estrutura de Decisão
Patos - PB | 2020

8 - Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
mesma é uma data válida.
"""

dia = int(input("Informe o dia: (DD) "))
mes = int(input("Informe o mês: (MM) "))
ano = int(input("Informe o ano: (AA) "))

validade = "inválida"

if (dia <= 31) and ((mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)):
    print("Entrei if 1")
    validade = "válida"
elif (dia <= 30) and (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Entrei if 2")
    validade = "válida"
elif (dia <= 29) and (mes == 2):
    if (ano%4==0 and ano%400!=0) or (ano%400==0):
        validade = "válida"
    elif dia <= 28:
        validade = "válida"
        

print("A data {}/{}/{} é {}".format(dia, mes, ano, validade))
