nota = float(input("Informe uma nota entre 0 e 10: "))
while nota < 0 or nota > 10:
    nota = float(input("Nota inválida! Informe uma entre 0 e 10 "))

print("A nota {} é válida! Ibrigado!".format(nota))
