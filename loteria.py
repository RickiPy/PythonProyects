# Programa que simula 20000 ganadores de lotería y muestra los números que más han ganado
import random
lista=[]
lol=""
listaaux=[]
for b in range(20000):

    for x in range(5):
        r=random.randint(0,9)
        lol+=str(r)
    lista.append(lol)
    lol=""
dicc={}
for b in lista:
    dicc[b]=0
    for a in lista:
        if b==a:
            dicc[b]+=1
for clave,valor in dicc.items():
    listaaux.append((valor,clave))
listaaux.sort(reverse=True)
for a in range(10):
    print(f"{listaaux[a][1]}---->{listaaux[a][0]}")