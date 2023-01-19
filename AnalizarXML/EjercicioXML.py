# Este programa, analiza datos de un xml, con el cual saca todas las tempertaruas minimas y medias, con la cual sacamos las medias anuales, analizamos las radiaciones de la cual sacamos la radiación máxima
# y el dia que se dió dicha radiación

import xml.etree.ElementTree as ET
import time
cont=0
lista=[]
radiaciones=[]
with open("Clim_Diario_2020.xml","r") as f:
    xml=f.read()
datos=ET.fromstring(xml)
Temp=datos.findall("Cns_OpenData/T_Min")
TempMed=datos.findall("Cns_OpenData/T_Med")
datos2=datos.findall("Cns_OpenData")
for a in range(len(Temp)):
    Temp[a]=float(Temp[a].text)
    TempMed[a]=float(TempMed[a].text)
for dato in datos2:
    try:
        if float(dato.find("PromedioDeRadiacion").text)>1.5:
            lista.append(dato.find("FECHA").text)
            radiaciones.append((float(dato.find("PromedioDeRadiacion").text),dato.find("FECHA").text[:10]))
            
    except AttributeError:
        pass
TempMinMedia=sum(Temp)/len(Temp)
TemMedAño=sum(TempMed)/len(TempMed)
radiaciones.sort(reverse=True)
while True:
    opcion=int(input("1.Media temperatura mínima anual\n2.Media temperatura media anual\n3.Fechas en las que se supera la radiación\n4.Número de días que se superó dicha radiación\n5.Radiación máxima\n6.Salir\nEntrada: "))
    if opcion==1:
        print(f"La media de la temperatura mínima anual es: {TempMinMedia:.2f}")
    if opcion==2:
        print(f"La media de la temperatura media anual es: {TemMedAño:.2f}")
    if opcion==3:
        for dato in lista:
            print(dato[:10])
    if opcion==4:
        print("La cantidad de días que se ha superado dicha radiación es: %d días"%(len(lista)))
    if opcion==5:
        print("El día con mayor radiación es %s con radiación %f"%(radiaciones[0][1],radiaciones[0][0]))
    if opcion==6:
        exit()
    time.sleep(4)
