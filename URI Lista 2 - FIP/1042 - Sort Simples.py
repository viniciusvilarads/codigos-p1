"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020

Leia 3 valores inteiros e ordene-os em ordem crescente. No 
final, mostre os valores em ordem crescente, uma linha em 
branco e em seguida, os valores na sequência como foram lidos.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1042

"""

N1, N2, N3 = input().split()
N1 = int(N1)
N2 = int(N2)
N3 = int(N3)
valores = list()
valores.append(N1)
valores.append(N2)
valores.append(N3)
valoresCobaia = valores[:]
valoresCobaia.sort()

for c in valoresCobaia:
    print(c)

print()

for c in valores:
    print(c)
