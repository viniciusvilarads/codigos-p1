"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1 URI
Patos - PB | 2020

Leia um valor inteiro, que é o tempo de duração em segundos de 
um determinado evento em uma fábrica, e informe-o expresso no 
formato horas:minutos:segundos.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1019

"""

N = int(input())

segundos = N % 60
minutos = (N // 60) % 60
horas = (N // 60) // 60

print("{}:{}:{}".format(horas, minutos, segundos))
