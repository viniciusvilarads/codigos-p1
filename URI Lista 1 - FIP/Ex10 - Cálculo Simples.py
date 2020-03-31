"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1 URI
Patos - PB | 2020

Neste problema, deve-se ler o código de uma peça 1, o 
número de peças 1, o valor unitário de cada peça 1, o 
código de uma peça 2, o número de peças 2 e o valor 
unitário de cada peça 2. Após, calcule e mostre o valor 
a ser pago.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1010

"""

peca1 = input().split()
peca2 = input().split()
qtdPeca1 = int(peca1[1])
valPeca1 = float(peca1[2])
qtdPeca2 = int(peca2[1])
valPeca2 = float(peca2[2])
TOTAL = (qtdPeca1 * valPeca1) + (qtdPeca2 * valPeca2)
print("VALOR A PAGAR: R$ {:.2f}".format(TOTAL))
