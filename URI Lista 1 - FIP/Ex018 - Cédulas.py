"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1 URI
Patos - PB | 2020

Leia um valor inteiro. A seguir, calcule o menor número de 
notas possíveis (cédulas) no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
A seguir mostre o valor lido e a relação de notas necessárias.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

"""

N = int(input())
N100 = 0
N50 = 0
N20 = 0
N10 = 0
N5 = 0
N2 = 0
N1 = 0
print(N)
while N >= 100:
    N100 = N100 + 1
    N = N - 100
while N >= 50:
    N50 = N50 + 1
    N = N - 50
while N >= 20:
    N20 = N20 + 1
    N = N - 20
while N >= 10:
    N10 = N10 + 1
    N = N - 10
while N >= 5:
    N5 = N5 + 1
    N = N - 5
while N >= 2:
    N2 = N2 + 1
    N = N - 2
while N >= 1:
    N1 = N1 + 1
    N = N - 1
print('{} nota(s) de R$ 100,00'.format(N100))
print('{} nota(s) de R$ 50,00'.format(N50))
print('{} nota(s) de R$ 20,00'.format(N20))
print('{} nota(s) de R$ 10,00'.format(N10))
print('{} nota(s) de R$ 5,00'.format(N5))
print('{} nota(s) de R$ 2,00'.format(N2))
print('{} nota(s) de R$ 1,00'.format(N1))
