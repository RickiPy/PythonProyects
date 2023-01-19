# En este programa, mediante expresiones irregulares creamos un patron de tal modo que nos saque todas las ips de un txt que se encuentra en una pagina web
from leercorreo import correos
import re
texto=correos()
texto=str(texto)
texto=texto.split("\n")
patron="\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\]"
for line in texto:
    de=re.search(patron,line)
    if de:
        ini=line.find("[")
        fin=line.find("]")
        print(line[ini+1:fin])