"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020



Você deve fazer um programa que leia um valor qualquer e 
apresente uma mensagem dizendo em qual dos seguintes 
intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se 
encontra. Obviamente se o valor não estiver em nenhum destes 
intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

O símbolo ( representa "maior que". Por exemplo:
[0,25]  indica valores entre 0 e 25.0000, inclusive eles.
(25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1037

"""

valor = float(input())

if 0 <= valor <= 25.0000:
    print("Intervalo [0,25]")
elif 25.00001 <= valor <= 50.0000000:
    print("Intervalo (25,50]")
elif 50.00000001 <= valor <= 75.0000000:
    print("Intervalo (50,75]")
elif 75.00000001 <= valor <= 100.0000000:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
