"""
Vinícius Vilar - ADS UNIFIP - Programação 1 - Lista 2 URI
Patos - PB | 2020

Pedrinho está organizando um evento em sua Universidade. O 
evento deverá ser no mês de Abril, iniciando e terminando 
dentro do mês. O problema é que Pedrinho quer calcular o 
tempo que o evento vai durar, uma vez que ele sabe quando 
inicia e quando termina o evento.

Sabendo que o evento pode durar de poucos segundos a vários 
dias, você deverá ajudar Pedrinho a calcular a duração deste 
evento.

Link: https://www.urionlinejudge.com.br/judge/pt/problems/view/1061


"""

di = input().split()
hIni = input().split(":")
df = input().split()
hFin = input().split(":")

di = int(di[1])
hi = int(hIni[0])
mi = int(hIni[1])
si = int(hIni[2])
df = int(df[1])
hf = int(hFin[0])
mf = int(hFin[1])
sf = int(hFin[2])

dia = df - di
hora = hf - hi    
minuto = mf - mi   
segundo = sf - si


if hora < 0:
    hora += 24
    dia -= 1
if minuto < 0:
    minuto += 60
    hora -= 1
if segundo < 0:
    segundo += 60
    minuto -=1
if dia <= 0:
    dia = 0

print("{} dia(s)".format(dia))
print("{} hora(s)".format(hora))
print("{} minuto(s)".format(minuto))
print("{} segundo(s)".format(segundo))
