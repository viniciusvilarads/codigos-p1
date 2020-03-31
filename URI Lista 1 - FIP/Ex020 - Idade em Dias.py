"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1 URI
Patos - PB | 2020

Leia um valor inteiro correspondente à idade de uma pessoa em 
dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 
365 dias e todo mês com 30 dias. Nos casos de teste nunca 
haverá uma situação que permite 12 meses e alguns dias, 
como 360, 363 ou 364. Este é apenas um exercício com 
objetivo de testar raciocínio matemático simples.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1020

"""

valor = int(input())

ano = valor // 365
mes = abs(((365 * ano) - valor)) // 30
dia = abs(((365 * ano) - valor)) % 30

print("{} ano(s)".format(ano))
print("{} mes(es)".format(mes))
print("{} dia(s)".format(dia))
