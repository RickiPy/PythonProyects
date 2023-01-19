# Este programa, se encarga de crear 20 numeros randoms de 0 a 100 los que son pares los mete en una carpeta llamada pares y los impares a otra llamada impares
# una vez generados estos números crea un txt con dicho número, y luego escribe en ese txt el numero, el numero al cuadrado y la raiz cubica del numero, controlando las excepciones
import os
import random

def crearTxT():
    try:
        os.makedirs("numeros")
        os.makedirs("numeros/pares")
        os.makedirs("numeros/impares")
    except FileExistsError:
        print("Ya existen las carpetas")
    for a in range(20):

        num=random.randint(0,100)
        if num%2==0:
            file=open("./numeros/pares/"+str(num)+".txt","w")
            file.write(f"{num}#{num**2}#{num**1/3}")
            file.close()
        else:
            file=open("./numeros/impares/"+str(num)+".txt","w")
            file.write(f"{num}#{num**2}#{num**1/3}")
            file.close()
def leerTxt():
    print("----NumerosPares----")
    for a in range(0,100,2):
        try:
            file=open("./numeros/pares/"+str(a)+".txt","r")
            file.close()
        except FileNotFoundError:
            print("Fichero "+str(a)+" no encontrado")
    print("----NumerosImpares----")
    for a in range(1,100,2):
        
        try:
            file=open("./numeros/impares/"+str(a)+".txt","r")
            file.close()
        except FileNotFoundError:
            print("Fichero "+str(a)+".txt no encontrado")
def imprimtxt():
    print("----NumerosPares----")
    for a in range(0,100,2):
        try:
            file=open("./numeros/pares/"+str(a)+".txt","r")
            f=file.read()
            f=f.split("#")
            print(f"El numero {f[0]}, el cuadrado {f[1]},la raiz cubica {float(f[2]):.2f}")
            file.close()
        except FileNotFoundError:
            print("Fichero "+str(a)+" no encontrado")
    print("----NumerosImpares----")
    for a in range(1,100,2):
        
        try:
            file=open("./numeros/impares/"+str(a)+".txt","r")
            f=file.read()
            f=f.split("#")
            print(f"El numero {f[0]}, el cuadrado {f[1]},la raiz cubica {float(f[2]):.2f}")
            file.close()
        except FileNotFoundError:
            print("Fichero "+str(a)+".txt no encontrado")
    
while True:
    opcion=int(input("1.Crear ficheros\n2.Comprobarlo\n3.Imprimir el texto de los ficheros existentes\n4.Salir\nEntrada: "))
    if opcion==1:
        crearTxT()
    if opcion==2:
        leerTxt()
    if opcion==3:
        imprimtxt()
    if opcion==4:
        break