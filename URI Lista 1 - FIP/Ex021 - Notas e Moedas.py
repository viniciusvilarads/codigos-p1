"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1 URI
Patos - PB | 2020

Leia um valor de ponto flutuante com duas casas decimais. 
Este valor representa um valor monetário. A seguir, calcule o 
menor número de notas e moedas possíveis no qual o valor pode 
ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2. 
As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. 
A seguir mostre a relação de notas necessárias.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

"""

N = float(input())
n100 = XVIDEO = n50 = n20 = n10 = n5 = n2 = m1 = m050 = m025 = m010 = m005 = m001 = 0
while True:
    if N >= 100:
        N = N - 100
        n100 = n100 + 1
    elif N >= 50:
        N = N - 50
        n50 = n50 + 1
    elif N >= 20:
        N = N - 20
        n20 = n20 + 1
    elif N >= 10:
        N = N - 10
        n10 = n10 + 1
    elif N >= 5:
        N = N - 5
        n5 = n5 + 1
    elif N >= 2:
        N = N - 2
        n2 = n2 + 1
    if N < 2:
        break
while N < 2 and N != 0:
    N = round(N, 2)
    if N >= 1:
        N = N - 1
        m1 = m1 + 1
    elif N < 1 and N >= 0.50:
        N = N - 0.50
        m050 = m050 + 1
    elif N >= 0.25:
        N = N - 0.25
        m025 = m025 + 1
    elif N >= 0.10:
        N = N - 0.10
        m010 = m010 + 1
    elif N >= 0.05:
        N = N - 0.05
        m005 = m005 + 1
    elif N >= 0.01:
        N = N - 0.01
        m001 = m001 + 1
print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(n100))
print('{} nota(s) de R$ 50.00'.format(n50))
print('{} nota(s) de R$ 20.00'.format(n20))
print('{} nota(s) de R$ 10.00'.format(n10))
print('{} nota(s) de R$ 5.00'.format(n5))
print('{} nota(s) de R$ 2.00'.format(n2))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(m1))
print('{} moeda(s) de R$ 0.50'.format(m050))
print('{} moeda(s) de R$ 0.25'.format(m025))
print('{} moeda(s) de R$ 0.10'.format(m010))
print('{} moeda(s) de R$ 0.05'.format(m005))
print('{} moeda(s) de R$ 0.01'.format(m001))
