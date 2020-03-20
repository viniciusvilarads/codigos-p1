"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 4 Estrutura de Decisão
Patos - PB | 2020

9 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a
quantidade de centenas, dezenas e unidades do mesmo.Observando os termos no
plural a colocação do "e", da vírgula entre outros.
Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades 
- Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21,
11, 1, 7 e 16
"""

numero = int(input("Informe um valor inteiro: "))
unidade = dezena = centena = 0
if  100 <= numero < 1000:
    unidade = numero % 10
    dezena = (numero // 10) % 10
    centena = numero // 100
elif 10 <= numero < 100:
    unidade = numero % 10
    dezena = numero // 10
elif numero < 10:
    unidade = numero

print("Centena {}".format(centena))
print("Dezena {}".format(dezena))
print("Unidade {}".format(unidade))
