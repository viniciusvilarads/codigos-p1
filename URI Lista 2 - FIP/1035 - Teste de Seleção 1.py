"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020

Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior 
do que C e se D for maior do que A, e a soma de C com D for 
maior que a soma de A e B e se C e D, ambos, forem positivos 
e se a variável A for par escrever a mensagem "Valores aceitos",
 senão escrever "Valores nao aceitos".

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1035

"""


A, B, C, D = input().split()
A = int(A)
B = int(B)
C = int(C)
D = int(D)

if ((B > C) and (D > A)) and ((C + D) > (A + B)) and (C > 0 and D > 0) and (A % 2 ==0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")

