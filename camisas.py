from sys import stdin, stdout
from collections import Counter

def cambiar_tallas(item):
    tabla_tallas = {
        32: "XS",
        36: "S",
        38: "M",
        40: "L",
        42: "XL",
        }

    return(
       tabla_tallas[item[0]], [item[1], item[1] * 12]
    )
        
    
lotes_usa = {
    "XS" : [0, 0],
    "S" : [0, 0],
    "M" : [0, 0],
    "L" : [0, 0],
    "XL" : [0, 0]
}

N = int(stdin.readline())

lotes_mxn = sorted(list(map(int, stdin.readline().split())))

total_lotes_mxn = Counter(lotes_mxn)
#stdout.write("lotes mxn: "+total_lotes_mxn.__str__()+"\n")


cambio_tallas = {k : v for k, v in map(cambiar_tallas, total_lotes_mxn.items())}
#stdout.write("cambio tallas: "+cambio_tallas.__str__()+"\n")
lotes_estandar_usa = {**lotes_usa, **cambio_tallas}
#stdout.write("lotes usa: "+lotes_estandar_usa.__str__()+"\n")

for k, v in lotes_estandar_usa.items():
    stdout.write("{}:{}:{}".format(k, v[0], v[1]).__str__()+"\n")
