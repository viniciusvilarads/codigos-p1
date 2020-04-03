"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020

Leia 2 valores com uma casa decimal (x e y), que devem 
representar as coordenadas de um ponto em um plano. 
A seguir, determine qual o quadrante ao qual pertence o ponto,
 ou se está sobre um dos eixos cartesianos ou na origem 
 (x = y = 0).

  Se o ponto estiver na origem, escreva a mensagem “Origem”.

Se o ponto estiver sobre um dos eixos escreva 
“Eixo X” ou “Eixo Y”, conforme for a situação.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1041

"""

x, y = input().split()
x = float(x)
y = float(y)

if x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")
elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")
elif ((x > 0) or (x < 0)) and y == 0:
    print("Eixo X")
elif ((y > 0) or (y < 0)) and x == 0:
    print("Eixo Y")
elif x == 0 and y == 0:
    print("Origem")
