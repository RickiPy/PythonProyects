# Este programa te geolocaliza cada ip que se encuentra en el txt
import geoip2.database

p=open("ips.txt","r")
ips=p.read()
p.close()
ips=ips.split("\n")
ips.pop(-1)
lista=[]
with geoip2.database.Reader("GeoLite2-City.mmdb") as localizar:
    for i in ips:
            try:
                ciudad = localizar.city(i)
                lista.append((str(ciudad.city.name),i))
            except geoip2.errors.AddressNotFoundError:
                print(f"No encontrado {i}")
print(lista)
