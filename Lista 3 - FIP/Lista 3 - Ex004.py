"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 3 Estrutura de Decisão
Patos - PB | 2020

4 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

"""


letra = input("Informe uma letra: ").upper()

if (letra == "A") or (letra == "E") or (letra == "I") or (letra == "O") or (letra == "U"):
    print("Vogal!")
else:
    print("Consoante!")
