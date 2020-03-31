"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1 URI
Patos - PB | 2020

Faça um programa que leia três valores e apresente o maior 
dos três valores lidos seguido da mensagem “eh o maior”. 
Utilize a fórmula:

MaiorAB = (a+b+abs(a-b))/2

Obs.: a fórmula apenas calcula o maior entre os dois primeiros 
(a e b). Um segundo passo, portanto é necessário para chegar 
no resultado esperado. 

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1013

"""

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
MaiorAB = (A+B+abs(A-B))/2
maior = int((MaiorAB+C+abs(MaiorAB-C))/2)
print("{} eh o maior".format(maior))
