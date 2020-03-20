"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 4 Estrutura de Decisão
Patos - PB | 2020

4 - Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente
e a mensagem "APROVADO" se o conceito for A, B ou C ou "REPROVADO" se o
conceito for D ou E.

"""

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2)/2

if 9 <= media <= 10:
    conceito = "A"
    situacao = "Aprovado"
elif 7.5 <= media < 9:
    conceito = "B"
    situacao = "Aprovado"
elif 6 <= media < 7.5:
    conceito = "C"
    situacao = "Aprovado"
elif 4 <= media < 6:
    conceito = "D"
    situacao = "Reprovado"
elif 0 <= media < 4:
    conceito = "E"
    situacao = "Reprovado"

print("Primeira nota: {:.1f}".format(nota1))
print("Segunda nota: {:.1f}".format(nota2))
print("Média: {:.1f}".format(media))
print("Conceito {}".format(conceito))
print("Situação: {}".format(situacao))
