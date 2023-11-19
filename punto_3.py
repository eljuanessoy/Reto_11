def matrizTranspuesta(m): #función que hace una matriz transpuesta
    resultado = []    
    for j in range(len(m[0])):
        fila = []
        for i in range(len(m)):
            fila.append(m[i][j]) #agregar el valor de la celda a la nueva fila
        resultado.append(fila)
    return resultado

m = []
f = int(input("Ingrese el número de filas de la matriz: "))  #se ingresa por parte del usuario la cantidad de filas de la matriz
c = int(input("Ingrese el número de columnas de la matriz: ")) #se ingresa por parte del usuario la cantidad de columnas de la matriz

for i in range(f):
    fila = []
    for j in range(c):
        valor = int(input(f"Ingrese el valor en la posición ({i}, {j}): "))
        fila.append(valor)
    m.append(fila)

print("Matriz ingresada: ") #se imprime la matriz ingresada
for fila in m:
    print(fila)

resultadoTranspuesta = matrizTranspuesta(m)  #se calcula la matriz transpuesta usando la funcion
print("Matriz transpuesta:") #se imprime la matriz transpuesta
for fila in resultadoTranspuesta:
    print(fila)