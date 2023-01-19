# En este programa, hacemos una busqueda mediante el metodo find con el cual marcamos un inicio y un final de la busqueda,
# la intención es simpplemente sacar todos los correos sin el dominio de un archivo txt que está en una página web y contarlos,
# el programa te ordena la cantidad de correos del que mas se encuentra al que menos y te los imprime

from leercorreo import correos

texto=correos()
texto=str(texto)
texto=texto.strip().split("\n")
correos1=[]
for a in range(len(texto)):
    inicio=texto[a].find("From")
    final=texto[a].find("@")
    if inicio != -1:
        correos1.append(texto[a][inicio+5:final])

for a in range(len(correos1)):
    correos1[a]=correos1[a].replace(" ","")
dicc={}
for b in correos1:
    dicc[b]=dicc.get(b,0)+1
lista=[]
for clave,valor in dicc.items():
    lista.append((valor,clave))
lista.sort(reverse=True)
print(lista)
for a in range(10):
    print(f"{lista[a][1]}---->{lista[a][0]}")
        
    
