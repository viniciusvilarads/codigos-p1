"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1
Patos - PB | 2020

3 - Em um banho de 5 minutos, fechando o registro ao se ensaboar, são gastos
45 litros de água. Sabendo que em 1 m3 de água há 1.000 litros, calcule
quantos banhos de 5 minutos são necessários para consumir 1 metro cúbico de
água?

"""


qtdBanho = 1000 / 45
valInteiro = 22 * 45
valArredondado = 23 * 45

print("22 banhos consomem {}L de água".format(valInteiro))
print("Para consumir exatos 1000L de água, são necessários {:.1f} banhos".format(qtdBanho))
print("23 banhos consome {}L de água".format(valArredondado))
