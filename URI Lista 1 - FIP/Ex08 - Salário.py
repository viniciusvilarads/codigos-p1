"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1 URI
Patos - PB | 2020

Escreva um programa que leia o número de um funcionário, 
seu número de horas trabalhadas, o valor que recebe por 
hora e calcula o salário desse funcionário. A seguir, 
mostre o número e o salário do funcionário, com duas casas 
decimais. 

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1008

"""

A = int(input())
B = int(input())
C = float(input())
SALARIO = B * C
print("NUMBER = {}".format(A))
print("SALARY = U$ {:.2f}".format(SALARIO))
