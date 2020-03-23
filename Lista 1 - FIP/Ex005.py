"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1
Patos - PB | 2020

5 - Receba do usuário o ano em que estamos, e o ano que ele nasceu, e calcule
sua idade. Despreze os meses.

"""


anoAtual = int(input("Informe o ano atual: "))
anoNascimento = int(input("Informe o ano de nascimento: "))
idade = anoAtual - anoNascimento

print("Sua idade é {} anos".format(idade))
