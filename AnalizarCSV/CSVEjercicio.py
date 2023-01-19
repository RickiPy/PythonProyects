# En este programa, sacamos las medias de un csv en el cual dispone de muchos datos
import csv
mascaros=[]
masbaratos=[]
mascarosP=[]
masbaratosP=[]
preciosaux=[]
habs=[]
m2=[]
signo=">"
with open("MadridAlquiler.csv", encoding="UTF-8") as fich:
    lineas=csv.reader(fich)
    lineas=list(lineas)
    lineas.pop(0)
    for linea in lineas:
        linea[2]=int(linea[2].replace("€/mes",""))
        preciosaux.append(linea[2])
        try:
            linea[3]=int(linea[3].replace(" hab.",""))
            habs.append(linea[3])
        except ValueError:
            print("No se encuentra el número de habitaciones")
        try:
            linea[4]=int(linea[4].replace(" m²",""))
            m2.append(linea[4])
        except ValueError:
            print("No se ha encontrado el valor de metros")
    lineas=sorted(lineas, key=lambda linea:linea[2])
    for line in range(10):
        masbaratos.append(lineas[line])
    for line in range(-1,-11,-1):
        mascaros.append(lineas[line])
    print("Pisos mas baratos")
    for piso in masbaratos:
        masbaratosP.append(piso[2])
        print(f"Piso: {piso[1]:<72}{signo:->10}{piso[2]}€")
    print("Pisos mas caros")
    
    for piso in mascaros:
        mascarosP.append(piso[2])
        print(f"Piso: {piso[1]:<72}{signo:->10}{piso[2]}€")
    print(f"Media de precios de los mas baratos: {sum(masbaratosP)/len(masbaratosP)}")
    print(f"Media de precios de los mas caros: {sum(mascarosP)/len(mascarosP)}")
    print(f"Media de las habitaciones: {sum(habs)/len(habs):.2f} habitaciones")
    print(f"Media de los metros cuadrados : {sum(m2)/len(m2):.2f}m²")
    

    

        
   