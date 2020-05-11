numeros = list()

for c in range(5):
    num = int(input("Informe o numero: "))
    numeros.append(num)

print("A soma dos valores é {}".format(sum(numeros)))
print("A média dos 5 valores é {:.2f}".format((sum(numeros))/5))
