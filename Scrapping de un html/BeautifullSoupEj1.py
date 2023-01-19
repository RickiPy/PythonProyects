# En este programa saco información de un documento html con el cual hago cálculos de medias, y lo reescribo en otro html en tablas.

from bs4 import BeautifulSoup as bs
Años=[]
Muertes=[]
InciAcc=[]
Datos=[]
with open("accidentes.html","r") as f:
    texto=f.read()
soup=bs(texto,"html.parser")
tabla=soup.find("table",{"id":"tablaBuena"})
tabla2=tabla.find_all("td")

for a in range(0,len(tabla2),3):Años.append(int(tabla2[a].text))
for a in range(1,len(tabla2),3):Muertes.append(int(tabla2[a].text))
for a in range(2,len(tabla2),3):InciAcc.append(int(tabla2[a].text))
for a in range(len(Años)):
    Datos.append([Años[a],Muertes[a],InciAcc[a]])
accid70s=0
accid80s=0
accid90s=0
accid2000s=0
accid2010s=0
muertes70s=0
muertes80s=0
muertes90s=0
muertes2000s=0
muertes2010s=0

for dato in Datos:
    if dato[0]<1980:
        accid70s+=dato[2]
        muertes70s+=dato[1]
    if dato[0]<1990 and dato[0]>1980:
        accid80s+=dato[2]
        muertes80s+=dato[1]
    if dato[0]<2000 and dato[0]>1990:
        accid90s+=dato[2]
        muertes90s+=dato[1]
    if dato[0]<2010 and dato[0]>2000:
        accid2000s+=dato[2]
        muertes2000s+=dato[1]
    if dato[0]<2020 and dato[0]>2010:
        accid2010s+=dato[2]   
        muertes2010s+=dato[1] 
        
mediaacc70s=accid70s/10
mediaacc80s=accid80s/10
mediaacc90s=accid90s/10
mediaacc2000s=accid2000s/10
mediaacc2010s=accid2010s/10
mediamuert70s=muertes70s/10
mediamuert80s=muertes80s/10
mediamuert90s=muertes90s/10
mediamuert2000s=muertes2000s/10
mediamuert2010s=muertes2010s/10

with open("medias.html","w") as f:
    f.write("""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style type="text/css">
       table, th, td {
        border: 1px solid;
        }
    </style>
    <title>Medias y total de accidentes por decada</title>
</head>
<table  id="tablaBuena">
        <thead>
        <tr>
        <th>Decada</th>
        <th>Media de muertes</th>
        <th>Media de accidentes</th>
        <th>Total de muertes</th>
        <th>Total de accidentes</th>
        </tr>
        </thead>
        <tbody><tr>
        <td align="right">70s</td>
        <td align="right">"""+str(mediamuert70s)+"""</td>
        <td align="right">"""+str(mediaacc70s)+"""</td>
        <td align="right">"""+str(muertes70s)+"""</td>
        <td align="right">"""+str(accid70s)+"""</td>
        </tr>
        <tr>
        <td align="right">80s</td>
        <td align="right">"""+str(mediamuert80s)+"""</td>
        <td align="right">"""+str(mediaacc80s)+"""</td>
        <td align="right">"""+str(muertes80s)+"""</td>
        <td align="right">"""+str(accid80s)+"""</td> 
        </tr>
        <tr>
        <td align="right">90s</td>
        <td align="right">"""+str(mediamuert90s)+"""</td>
        <td align="right">"""+str(mediaacc90s)+"""</td>
        <td align="right">"""+str(muertes90s)+"""</td>
        <td align="right">"""+str(accid90s)+"""</td>  
        </tr>
        <tr>
        <td align="right">2000s</td>
        <td align="right">"""+str(mediamuert2000s)+"""</td>
        <td align="right">"""+str(mediaacc2000s)+"""</td>
        <td align="right">"""+str(muertes2000s)+"""</td>
        <td align="right">"""+str(accid2000s)+"""</td> 
        </tr>
        <tr>
        <td align="right">2010s</td>
        <td align="right">"""+str(mediamuert2010s)+"""</td>
        <td align="right">"""+str(mediaacc2010s)+"""</td>
        <td align="right">"""+str(muertes2010s)+"""</td>
        <td align="right">"""+str(accid2010s)+"""</td>  
        </tr>
        </table>""")



