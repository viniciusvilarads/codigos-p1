"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020



Leia quatro números (N1, N2, N3, N4), cada um deles com uma 
casa decimal, correspondente às quatro notas de um aluno. 
Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para 
cada uma destas notas e mostre esta média acompanhada pela 
mensagem "Media: ". Se esta média for maior ou igual a 7.0, 
imprima a mensagem "Aluno aprovado.". Se a média calculada for 
inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a 
média calculada for um valor entre 5.0 e 6.9, inclusive estas, 
o programa deve imprimir a mensagem "Aluno em exame.".

No caso do aluno estar em exame, leia um valor correspondente 
à nota do exame obtida pelo aluno. Imprima então a mensagem 
"Nota do exame: " acompanhada pela nota digitada. Recalcule a 
média (some a pontuação do exame com a média anteriormente 
calculada e divida por 2). e imprima a mensagem 
"Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou 
"Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). 
Para estes dois casos (aprovado ou reprovado após ter pego 
exame) apresente na última linha uma mensagem 
"Media final: " seguido da média final para esse aluno.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1040

"""


N1, N2, N3, N4 = input().split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1))/10

print("Media: {:.1f}".format(media))

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
elif 5.0 <= media <= 6.9:
    print("Aluno em exame.")
    nExame = float(input())
    print("Nota do exame: {:.1f}".format(nExame))
    novaMedia = (nExame + media)/2
    if novaMedia >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(novaMedia))
