"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020

Leia um valor inteiro entre 1 e 12, inclusive. Correspondente 
a este valor, deve ser apresentado como resposta o mês do ano 
por extenso, em inglês, com a primeira letra maiúscula.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1052

"""

m = int(input())

mes = ["January", "February", "March", "April", "May", "June", "July", "August",
       "September", "October", "November", "December"]

print(mes[m-1])
