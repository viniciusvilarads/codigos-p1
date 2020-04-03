"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020

Neste problema, você deverá ler 3 palavras que definem o tipo 
de animal possível segundo o esquema abaixo, da esquerda para 
a direita.  Em seguida conclua qual dos animais seguintes foi 
escolhido, através das três palavras fornecidas. 

IMAGEM NA QUESTÃO

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1049

"""

coluna = input()
tipo = input()
comida = input()

if comida == "carnivoro":
    print("aguia")
elif tipo == "ave" and comida == "onivoro":
    print("pomba")
elif tipo == "mamifero" and comida == "onivoro":
    print("homem")
elif tipo == "anelideo" and comida == "onivoro":
    print("minhoca")
elif tipo == "mamifero" and comida == "herbivoro":
    print("vaca")
elif tipo == "inseto" and comida == "herbivoro":
    print("lagarta")
elif tipo == "inseto" and comida == "hematofago":
    print("pulga")
elif tipo == "anelideo" and comida == "hematofago":
    print("sanguessuga")
