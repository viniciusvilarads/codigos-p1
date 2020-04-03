"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020

Com base na tabela abaixo, escreva um programa que leia o 
código de um item e a quantidade deste item. A seguir, 
calcule e mostre o valor da conta a pagar.

IMAGEM NA QUESTÃO

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1038

"""

cod, qtd = input().split()
cod = int(cod)
qtd = int(qtd)

if cod == 1:
    preco = 4.00 * qtd
elif cod == 2:
    preco = 4.50 * qtd
elif cod == 3:
    preco = 5.00 * qtd
elif cod == 4:
    preco = 2.00 * qtd
elif cod == 5:
    preco = 1.50 * qtd

print("Total: R$ {:.2f}".format(preco))
