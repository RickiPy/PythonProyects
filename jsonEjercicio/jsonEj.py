# Este programa saca datos de un .json con el cual imprimos información que nos interesa mas legible para el ser humano, y hacemos calculos como contar cuantas canciones tiene cada artista
import json
with open("metallica-albums.json","r")as f:
    texto=f.read()
info=json.loads(texto)
def listar():
    for dato in info:
        cont=1
        print(f"Nombre: {dato['name']}")
        print(f"Fecha: {dato['year']}")
        for dat in dato["songs"]:
            print(f"Cancion {cont}. {dat['name']}")
            cont+=1
def contar():
    for dato in info:
        lista=[]
        for dat in dato['songs']:
            lista.append(dat['name'])
        print(f"Nombre--->{dato['name']:<32}Numero de canciones--->{len(lista)}")
        lista.clear()   
while True:         
    opcion=int(input("1.Listar información\n2.Contar información\n3.Salir\nEntrada: "))
    if opcion==1:
        listar()
    if opcion==2:
        contar()
    if opcion==3:
        exit()