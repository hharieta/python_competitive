lotes_usa = {
    "XS" : [0, 0],
    "S" : [0, 0],
    "M" : [0, 0],
    "L" : [0, 0],
    "XL" : [0, 0]
}

contar_lotes = {
        32: 0,
        36: 0,
        38: 0,
        40: 0,
        42: 0
    }

tabla_tallas ={
    32: "XS",
    36: "S",
    38: "M",
    40: "L",
    42: "XL"
}

N = int(input())

lotes_mxn = list(map(int, input().split()))

for i in range(N):
    # print(lotes_mxn[i])
    if lotes_mxn[i] in contar_lotes.keys():
        # print(tabla_tallas[lotes_mxn[i]])
        contar_lotes[lotes_mxn[i]] = contar_lotes[lotes_mxn[i]]+1

#print("contar lotes items: ", contar_lotes)

for k, v in contar_lotes.items():
    #print("contar lotes k: ", k)
    #print("contar lotes v: ", v)
    if k in tabla_tallas.keys():
        lotes_usa[tabla_tallas[k]] = [v, v*12]

#print(contar_lotes)
for k, v in lotes_usa.items():
    print("{}:{}:{}".format(k, v[0], v[1]))


