"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 3 Estrutura de Decisão
Patos - PB | 2020

5 - Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.

"""


nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2)/2
situacao = ""

if media == 10:
    situacao = "Aprovado com Distinção"
elif 7 <= media < 10:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print("Média: {:.1f}".format(media))
print("Situação: {}".format(situacao))
