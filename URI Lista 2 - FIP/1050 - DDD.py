"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020

Leia um número inteiro que representa um código de DDD para 
discagem interurbana. Em seguida, informe à qual cidade o DDD 
pertence, considerando a tabela abaixo:

IMAGEM NA QUESTÃO

Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1050

"""

ddd = int(input())

if ddd == 61:
    print("Brasilia")
elif ddd == 71:
    print("Salvador")
elif ddd == 11:
    print("Sao Paulo")
elif ddd == 21:
    print("Rio de Janeiro")
elif ddd == 32:
    print("Juiz de Fora")
elif ddd == 19:
    print("Campinas")
elif ddd == 27:
    print("Vitoria")
elif ddd == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")
