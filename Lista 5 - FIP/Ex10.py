num1 = int(input("Informe um número: "))
num2 = int(input("Informe outro número: "))

for c in range(min(num1, num2)+1, max(num1, num2)):
    print(c)
