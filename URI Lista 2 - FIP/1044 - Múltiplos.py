"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020

Leia 2 valores inteiros (A e B). Após, o programa deve mostrar 
uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando 
se os valores lidos são múltiplos entre si.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

"""

A, B = input().split()
A = int(A)
B = int(B)
if max(A,B) % min(A,B) == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
