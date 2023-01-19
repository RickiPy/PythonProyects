# En este programa, es un gestor de alumnos en el cual puedes insertar nuevos alumnos, ver las notas de cada alumno, ver las notas medias, ver los alumnos suspendidos y aprobados
# Interfaz muy interactiva jugando y formateando con los Strings, de nuevo usamos listas como base de datos

import os
DataBase=[]
def menu():
    print("1.Insertar Alumno")
    print("2.Todas las notas")
    print("3.Notas medias por trimestres")
    print("4.Suspensos aprobados")
    print("5.Salir")
    opcion=int(input("Selecciona la opción: "))
    if opcion==1:
        insertAlumn()
    if opcion==2:
        TodasNotas()
    if opcion==3:
        NotasMediasT()
    if opcion==4:
        SuspensosAprobados()
    if opcion==5:
        exit()
def insertAlumn():
    os.system("cls")
    NombreAl=input("Dime el nombre: ")
    Apellido=input("Apellido: ")
    DNI=input("DNI: ")
    Notas=input("Introduce las notas por espacios:\n")
    Notas=Notas.split(" ")
    i=0
    while i<len(Notas):
        if Notas[i].isdigit()==False:
            Notas.pop(i)
            i-=1
        i+=1    
    
    if len(Notas)<10:
        cont=10-len(Notas)
        for b in range(cont):
            Notas.append("0")
    else:
        cont=len(Notas)-10
        for a in range(cont):
            Notas.pop(0)
    for a in range(len(Notas)):
        Notas[a]=int(Notas[a])
    
    NotasTri=Notas[7:10]
    NotasPrac=Notas[0:7]
    NotFinal=((sum(NotasPrac)/7)*0.3)+((sum(NotasTri)/3)*0.7)
    DataBase.append([NombreAl,Apellido,DNI,NotFinal,NotasTri])
    os.system("cls")
    menu()
def TodasNotas():
    print("+--------------------+--------------------+--------------------+--------------------+")
    print("|Nombre              |Apellido            |DNI                 |Nota Final          |")
    print("+--------------------|--------------------|--------------------|--------------------+")
    for a in range(len(DataBase)):

        print("|{:<20}|{:<20}|{:<20}|{:<20.2f}|".format(DataBase[a][0],DataBase[a][1],DataBase[a][2],DataBase[a][3]))
        print("+--------------------+--------------------+--------------------+--------------------+")
    opcion=int(input("Para volver a menu 1: "))
    if opcion==1:
        os.system("cls")
        menu()   
def NotasMediasT():
    TotalPT=0
    TotalST=0
    TotalTT=0
    for a in range(len(DataBase)):
        TotalPT+=DataBase[a][4][0]
    for b in range(len(DataBase)):
        TotalST+=DataBase[b][4][1]
    for c in range(len(DataBase)):
        TotalTT+=DataBase[c][4][2]
    MediaPT=TotalPT/len(DataBase)
    MediaST=TotalST/len(DataBase)
    MediaTT=TotalTT/len(DataBase)
    print("+--------------------+--------------------+--------------------+")
    print("|Primer trimestre    |Segundo trimestre   |Tercer trimestre    |")
    print("+--------------------+--------------------+--------------------+")
    print("|{:<20.2f}|{:<20.2f}|{:<20.2f}|".format(MediaPT,MediaST,MediaTT))
    opcion=(int(input("Para volver a menu 1: ")))
    if opcion==1:
        os.system("cls")
        menu()
def SuspensosAprobados():
    print("+--------------------+----------------APROBADOS----------------+--------------------+")
    print("|Nombre              |Apellido            |DNI                 |Nota Final          |")
    print("+--------------------|--------------------|--------------------|--------------------+")
    for a in range(len(DataBase)):
        if DataBase[a][3]>5:
            print("|{:<20}|{:<20}|{:<20}|{:<20.2f}|".format(DataBase[a][0],DataBase[a][1],DataBase[a][2],DataBase[a][3]))
            print("+--------------------+--------------------+--------------------+--------------------+")   
    print("+--------------------+----------------SUSPENSOS----------------+--------------------+")
    for a in range(len(DataBase)):
        if DataBase[a][3]<5:
            print("|{:<20}|{:<20}|{:<20}|{:<20.2f}|".format(DataBase[a][0],DataBase[a][1],DataBase[a][2],DataBase[a][3]))
            print("+--------------------+--------------------+--------------------+--------------------+") 
    opcion=(int(input("Para volver a menu 1: ")))
    if opcion==1:
        os.system("cls")
        menu()
menu()