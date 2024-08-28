#arreglo bidimencional 3*3
arreglo_bidim= [
    [5, 10, 15], # indice 0
    [20, 25, 30], # indice 1
    [35, 40, 45] # indice 3
]
# Busqueda de un valor especifico en arreglo bidimencional
valor_buscado= 40
if any(valor_buscado in fila for fila in arreglo_bidim):
    print(f"se encontro {valor_buscado} en arreglo bidimencional")
else:
    print(f"{valor_buscado} no se encontro en arreglo bidimencional")