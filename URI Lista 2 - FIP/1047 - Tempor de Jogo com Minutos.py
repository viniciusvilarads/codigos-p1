"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020


Leia a hora inicial, minuto inicial, hora final e minuto final 
de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração 
máxima de 24 horas.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1047

"""

hInicial, mInicial, hFinal, mFinal = input().split()
hInicial = int(hInicial)
mInicial = int(mInicial)
hFinal = int(hFinal)
mFinal = int(mFinal)


if hFinal > hInicial:
    hora = hFinal - hInicial
    if mFinal > mInicial:
        minuto = mFinal - mInicial
    elif mInicial > mFinal:
        hora = hora - 1
        minuto = (60 - mInicial) + mFinal
    elif mInicial == mFinal:
        minuto = 0
elif hInicial > hFinal:
    hora = (24 - hInicial) + hFinal
    if mFinal > mInicial:
        minuto = mFinal - mInicial
    elif mInicial > mFinal:
        hora = hora - 1
        minuto = (60 - mInicial) + mFinal
    elif mInicial == mFinal:
        minuto = 0
elif hInicial == hFinal:
    if mFinal > mInicial:
        minuto = mFinal - mInicial
        hora = 0
    elif mInicial > mFinal:
        minuto = (60 - mInicial) + mFinal
        hora = 23
    elif mInicial == mFinal:
        hora = 24
        minuto = 0

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora, minuto))
