"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 3 Estrutura de Decisão
Patos - PB | 2020

3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

"""

sexo = input("Informe o sexo: [M/F] ").upper()
valSexo = ""

if sexo == "M":
    valSexo = "Masculino"
elif sexo == "F":
    valSexo = "Feminino"
else:
    valSexo = "Inválido"

print("Sexo {}".format(valSexo))
