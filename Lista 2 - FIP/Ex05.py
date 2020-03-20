"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 4 Estrutura de Decisão
Patos - PB | 2020



"""

valDivida = float(input("Informe o valor da dívida: R$"))
diaAtraso = int(input("Quantos dias em atraso: "))
valDia = float(input("Qual o valor por dia de atraso: R$"))

valMulta = diaAtraso * valDia
valPagar = valDivida + valMulta

print("O valor da multa é de R${:.2f}.".format(valMulta))
print("Será necessário pagar esse valor, mais o valor da dívida. Totalizando R${:.2f}".format(valPagar))
