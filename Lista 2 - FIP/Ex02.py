"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 4 Estrutura de Decisão
Patos - PB | 2020

2. Em um banho de 5 minutos, fechando o registro ao se ensaboar, são gastos
45 litros de água. Sabendo que em 1 m3 de água há 1.000 litros, calcule
quantos banhos de 5 minutos são necessários para consumir 1 metro cúbico
de água?

"""


gastoAgua = 1 / 0.045
valInteiro = int(gastoAgua)

print("### Em um banho de 5 minutos, gastando 45 litros de água!### ")
print("São necessário {} banhos para gastar 990L de água!".format(valInteiro))
print("Para consumir 1m^3 de água (1.000 litros), são necessário {:.2f} banhos!".format(gastoAgua))

print()
print("-"*60)
print()

tempoBanho = int(input("Quanto tempo demora no banho: "))
agua = tempoBanho * 9

print("Em um banho de de {} são gastos {}L de água!".format(tempoBanho, agua))

