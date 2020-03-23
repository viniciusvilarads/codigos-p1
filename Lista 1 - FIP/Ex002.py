"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 1
Patos - PB | 2020

2 - Sabendo que a cotação atual do dólar americano é R$ 4,47, receba um valor
em reais do usuário e converta para dólares. Exemplo de saída: $ 1.00

"""


real = float(input("Informe o valor em reais R$"))
realDolar = real / 4.47

print("Cotação atual do dólar U$4.47")
print("R${:.2f} equivale a U${:.2f}".format(real, realDolar))
