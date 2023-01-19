# Este programa, mediante expresiones irregulares busca todas las ips, las escribe y quitas las repetidas en un txt
import re
f=open("mbox-short.txt","r")
texto=f.read()
f.close()
texto=texto.split("\n")
patron="\[\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\]"
ips=[]
l=open("ips.txt","w")
for line in texto:
    de=re.search(patron,line)
    if de:
        ini=line.find("[")
        fin=line.find("]")
        ip=line[ini+1:fin]
        ips.append(ip)
ips=set(ips)
for dato in ips:
    l.write(dato+"\n")
l.close()