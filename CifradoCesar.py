# En este programa, se pide un desplazamiento que se encargará de sumar en ASCII cada valor de cada caracter de tal forma que el texto estará cifrado
# y luego te lo imprimirá la palabra sin cifrar con su determinada palabra cifrada.

lista=[]
c1=True
desp=int(input("Dime el desplazamiento"))
while c1:
    cadena=input("Cadena: ")
    if cadena.startswith("#"):
        continue
    if cadena == "FIN" or cadena =="fin":
        break
    lista.append(cadena)
i=0
while i<len(lista):
    a=0
    cifrado=""
    while a<len(lista[i]):
        cifrado+=(chr(ord(lista[i][a])+desp))
        
        a+=1
    print(lista[i]+"---->"+cifrado)
    i+=1
