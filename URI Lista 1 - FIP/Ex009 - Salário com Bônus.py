"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1 URI
Patos - PB | 2020

Faça um programa que leia o nome de um vendedor, o seu salário
fixo e o total de vendas efetuadas por ele no 
mês (em dinheiro). Sabendo que este vendedor 
ganha 15% de comissão sobre suas vendas efetuadas, 
informar o total a receber no final do mês, com duas casas 
decimais.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1009

"""

nome = input()
salario = float(input())
vendas = float(input())
novoSalario = ((15 * vendas)/100) + salario
print("TOTAL = R$ {:.2f}".format(novoSalario))
