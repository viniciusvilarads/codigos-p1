"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 4 Estrutura de Decisão
Patos - PB | 2020

1 - As Organizações Tabajara resolveram dar um aumento de salário aos seus
colaboradores e lhe contraram para desenvolver o programa que calculará os
reajustes.
- Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
-- salários até R$ 280,00 (incluindo) : aumento de 20%
-- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
-- o salário antes do reajuste;
-- o percentual de aumento aplicado;
-- o valor do aumento;
-- o novo salário, após o aumento.

"""


salario = float(input("Informe o seu salário: "))

if 0 < salario <= 200:
    percReaj = "20%"
    reaj = (salario * 20)/100
    novoSalario = salario + reaj
elif 200 < salario <= 700:
    percReaj = "15%"
    reaj = (salario * 15)/100
    novoSalario = salario + reaj
elif 700 < salario <= 1500:
    percReaj = "10%"
    reaj = (salario * 10)/100
    novoSalario = salario + reaj
elif salario > 1500:
    percReaj = "5%"
    reaj = (salario * 5)/100
    novoSalario = salario + reaj
else:
    print("valor informado foi 0 ou abaixo de 0")
    percReaj = "0%"
    reaj = 0
    novoSalario = 0


print("Salário: R%{:.2f}".format(salario))
print("Reajuste de {}".format(percReaj))
print("Valor do reajuste: R${:.2f}".format(reaj))
print("Novo salário: R${:.2f}".format(novoSalario))
