"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020



Leia 3 valores reais (A, B e C) e verifique se eles formam ou 
não um triângulo. Em caso positivo, calcule o perímetro do 
triângulo e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B 
como base e C como altura, mostrando a mensagem

Area = XX.X

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1043


"""


l1, l2, l3 = input().split()
l1 = float(l1)
l2 = float(l2)
l3 = float(l3)

if ((l1 + l2) > l3) and ((l1 + l3) > l2) and ((l2 + l3) > l1):
    perimetro = l1 + l2 + l3
    print("Perimetro = {:.1f}".format(perimetro))
else:
    area = ((l1+l2)*l3)/2
    print("Area = {:.1f}".format(area))
