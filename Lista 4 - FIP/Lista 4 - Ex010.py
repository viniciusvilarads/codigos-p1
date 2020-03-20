"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 4 Estrutura de Decisão
Patos - PB | 2020

10 - Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:
- A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva
média alcançada;
- A mensagem "Reprovado", se a média for menor do que 7, com a respectiva
média alcançada;
- A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""


nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

print("Média: {:.1f}".format(media))

if media == 10:
    situacao = "Aprovado com Distinção!"
elif media >= 7:
    situacao = "Aprovado!"
elif media < 7:
    situacao = "Reprovado!"

print(situacao)
