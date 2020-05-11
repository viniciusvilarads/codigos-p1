popA = int(input("Informe a quantidade de habitantes da População A: "))
taxA = float(input("Taxa de crescimento da população A: "))
popB = int(input("Informe a quantidade de habitantes da População B: "))
taxB = float(input("Taxa de crescimento da população B: "))
ano = 0
while popA < popB:
    popA += (popA * taxA) / 100
    popB += (popB * taxB) / 100
    ano += 1

print("População A: {:.2f}".format(popA))
print("População B: {:.2f}".format(popB))
print("Foram ncessário {} anos para a população A ultrapassar ou igualar a população B".format(ano))


