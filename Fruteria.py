# Este programa, es una interfaz de una frutería la cual se puede añadir productos, ver las ventas, buscar productos, y crear tickets, se usa una lista como base de datos

def menu(fruteria):
    print("1.Añadir productos")
    print("2.Ventas")
    print("3.Buscar producto")
    print("4.Crear ticket")
    print("5.Salir")
    opcion=int(input("Entrada: "))
    if opcion==1:
        AñadProd(fruteria)
    if opcion==2:
        Ventas(ProductosVendidos,fruteria)
    if opcion==3:
        BuscProd(ProductosVendidos)
    if opcion==4:
        CrearTick(fruteria,carrito,ProductosVendidos)
    if opcion==5:
        exit()
def AñadProd(fruteria):
    print("+-------------------------------------+")
    print("|Producto  |Precio/kg |Cantidad de kg |")
    print("+-------------------------------------+")
    for clave,valor in fruteria.items():
        print("|{:<10}|{:<6}€/kg|{:<13}kg|".format(clave,valor[0],valor[1]))
        print("+-------------------------------------+")
    print("")
    print("1.Para añadir producto")
    print("2.Para modificar un producto")
    print("3.Eliminar producto")
    print("4.Volver menu")
    opcion=int(input("Entrada: "))
    if opcion==1:
        nom=input("Escribe el nombre de la fruta: ")
        precio=float(input("Escribre el precio de la fruta: "))
        cantK=float(input("Cuantos kilos va a añadir: "))
        fruteria[nom]=[precio,cantK]
        ProductosVendidos[nom]=[0]
        opcion=int(input("1 para volver:  "))
        if opcion==1:
            menu(fruteria)
        
    if opcion==2:
        nom=input("Escribe el nombre de la fruta que va a modificar: ")
        print("1.Cambiar nombre")
        print("2.Cambiar precio")
        print("3.Cambiar cantidad kg")
        opcion2=int(input("Entrada: "))
        if opcion2==1:
            nomn=input("Nuevo nombre: ")
            fruteria[nomn]=fruteria[nom]
            del(fruteria[nom])
            print("Se ha modificado correctamente")
            opcion2=int(input("1 para volver:  "))
            if opcion==1:
                menu(fruteria)
        if opcion2==2:
            precio=float(input("Nuevo precio por kilo: "))
            fruteria[nom]=precio
            print("Se ha modificado correctamente")
            opcion2=int(input("1 para volver:  "))
            if opcion2==1:
                menu(fruteria)
        if opcion2==3:
            cant=float(input("Nueva cantidad: "))
            fruteria[nom][1]=cant
            print("Se ha modificado correctamente")
            opcion2=int(input("1 para volver:  "))
            if opcion2==1:
                menu(fruteria)
    if opcion==3:
        print("Si no quieres eliminar ningun producto,escribe 0")
        frut=input("Nombre de la fruta que va a eliminar: ")
        if frut=="0":
            AñadProd(fruteria)
        if frut in fruteria:
            del(fruteria[frut])
            print("Fruta eliminada correctamente.")
            opcion=int(input("1 para volver:  "))
            if opcion==1:
                menu(fruteria)
        else:
            print("No existe la fruta que queires eliminar")
    if opcion==4:
        menu(fruteria)
            
    return fruteria
def Ventas(ProductosVendidos,fruteria):
    guion="-"
    print(f"+{guion:-<72}+")
    print("|Nombre    |Kilogramos vendidos   |Cantidad almacenada   |Dinero ganado  |")
    print(f"+{guion:-<72}+")
    for clave,valor in ProductosVendidos.items():
        if valor[0]>0:
            print(f"|{clave:<10}|{valor[0]:<22}|{valor[2]:<22}|{(valor[0]*valor[1]):<15.2f}|")
            print(f"+{guion:-<72}+")
def BuscProd(ProductosVendidos):
    guion="-"
    encontrado=input("Dime el producto del que quieres información: ") 
    print(f"+{guion:-<72}+")
    print("|Nombre    |Kilogramos vendidos   |Cantidad almacenada   |Dinero ganado  |")
    print(f"+{guion:-<72}+")
    
    for clave in ProductosVendidos.keys():
        if clave==encontrado:

            print(f"|{clave:<10}|{ProductosVendidos[clave][0]:<22}|{ProductosVendidos[clave][2]:<22}|{(ProductosVendidos[clave][0]*ProductosVendidos[clave][1]):<15.2f}|")
            print(f"+{guion:-<72}+")
        
    
def CrearTick(fruteria,carrito,ProductosVendidos):
    print("1.Añadir al carrito")
    print("2.Finalizar compra")
    
    
    opcion=int(input("Entrada: "))
    if opcion==1:
        a=0
        for clave,valor in fruteria.items():
            print(f"{a+1}.{clave:-<18}>{valor[0]:.2f} €/kg")
            a+=1
        print("Escriba 0 para finalizar la compra")
        while True:
            lista=list(fruteria.items())
            entrada=int(input("Entrada: "))
            if entrada==0:
                CrearTick(fruteria,carrito,ProductosVendidos)
                break
            kilos=float(input("Cantidad de kilos: "))
            precio=kilos*lista[entrada-1][1][0]
            carrito.append([lista[entrada-1][0],precio,kilos])
            ProductosVendidos[lista[entrada-1][0]][0]=ProductosVendidos[lista[entrada-1][0]][0]+kilos
            
            
    if opcion==2:
        texto="Ticket"
        texto2="Total sin iva"
        texto3="Total con iva"
        guion="-"
        total=[]
        print(f"+{texto:-^32}+")
        print(f"|Nombre    |Cantidad   |Precio   |")
        print(f"|{guion:-<32}|")
        for valor in carrito:
            print(f"|{valor[0]:<10}|{valor[2]:<9.2f}Kg|{valor[1]:<8.2f}€|")
            total.append(valor[1])
        print(f"|{guion:-<32}|")
        print(f"|{texto2:.<26}{sum(total):<5.2f}€|")
        print(f"|{texto3:.<26}{(sum(total))*1.08:<5.2f}€|")
        print(f"+{guion:-<32}+")
        
        opcion3=int(input("1 para volver\nEntrada: "))
        if opcion3==1:
            carrito.clear()
            menu(fruteria)
    
    return carrito,ProductosVendidos
        
              

    
        

fruteria={"Manzanas":[1.25,30],"Peras":[1.95,40],"Platanos":[2.50,10]}

carrito=[]
ProductosVendidos={}
for clave,valor in fruteria.items():
        ProductosVendidos[clave]=[0,valor[0],valor[1]]

menu(fruteria)