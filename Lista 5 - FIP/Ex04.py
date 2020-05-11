popA = 80000
popB = 200000
ano = 0
while popA < popB:
    popA += (popA * 3) / 100
    popB += (popB * 1.5) / 100
    ano += 1

print("População A: {:.2f}".format(popA))
print("População B: {:.2f}".format(popB))
print("Foram ncessário {} anos para a população A ultrapassar ou igualar a população B".format(ano))


