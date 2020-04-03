"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020

Leia a hora inicial e a hora final de um jogo. A seguir 
calcule a duração do jogo, sabendo que o mesmo pode começar 
em um dia e terminar em outro, tendo uma duração mínima 
de 1 hora e máxima de 24 horas.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1046

"""


A, B = input().split()
A = int(A)
B = int(B)

if A > B:
    A = 24 - A
    hora = A + B
elif A < B:
    hora = B - A
else:
    hora = 24

print("O JOGO DUROU {} HORA(S)".format(hora))
