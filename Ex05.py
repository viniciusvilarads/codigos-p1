"""
5. Faça um programa que calcule o valor a ser pago por uma dívida em atraso.
O usuário deve informar o valor original da dívida (ex. R$ 50,00), a
quantidade de dias em atraso (ex. 35 dias) e o valor da multa por dia de
atraso (ex. R$ 0,25).
"""

valDivida = float(input("Informe o valor da dívida: R$"))
diaAtraso = int(input("Quantos dias em atraso: "))
valDia = float(input("Qual o valor por dia de atraso: R$"))

valMulta = diaAtraso * valDia
valPagar = valDivida + valMulta

print("O valor da multa é de R${:.2f}.".format(valMulta))
print("Será necessário pagar esse valor, mais o valor da dívida. Totalizando R${:.2f}".format(valPagar))
