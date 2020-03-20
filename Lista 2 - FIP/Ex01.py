"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 Estrutura de Decisão
Patos - PB | 2020

1. Faça um programa que solicite ao usuário o valor do litro de combustível
(ex. 4,75) e quanto em dinheiro ele deseja abastecer (ex. 50,00). Calcule
quantos litros de combustível o usuário obterá com esses valores.

"""
valor = float(input("Informe o valor do combustível: R$"))
combust = float(input("Informe quanto deseja adicionar ao veículos: R$"))

qtdCombust = combust / valor

print("Foi adicionado {:.2f}L de combustível!".format(qtdCombust))
