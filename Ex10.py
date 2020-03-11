"""
10. Faça um programa que calcula o novo valor do salário de um funcionário.
O usuário informa o salário atual (ex. 1250,00) e o percentual do reajuste
(ex. 13,5 %).
"""

sal = float(input("Informe seu salário: R$"))
reaj = float(input("Informe o valor do reajuste: %"))

valReaj = (reaj * sal) / 100
novoSal = sal + valReaj

print("Reajute de {}% equivalente a R${:.2f}".format(reaj, valReaj))
print("Novo salário com reajuste R${:.2f}".format(novoSal))
