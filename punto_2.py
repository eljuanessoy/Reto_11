def Matriz(fil, colum):  #aqui seran ingresados y almacenados los valores de la matriz
    matriz = []
    for i in range(fil):
        fila = []
        for j in range(colum):
            valor = int(input(f"Ingrese el valor en la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def multiplicar(mA, mB):  #función que multiplica las dos matrices (A y B)
    f1 = len(mA)
    c2 = len(mB[0])
    resultado = [[0] * c2 for i in range(f1)]
    for i in range(f1):
        for j in range(c2):
            for k in range(len(mB)):
                resultado[i][j] += mA[i][k] * mB[k][j]
    return resultado

f1 = int(input("Ingrese el número de filas de la matriz A: ")) #se ingresa por parte del usuario la cantidad de filas de la matriz A
c1 = int(input("Ingrese el número de columnas de la matriz A: ")) #se ingresa por parte del usuario la cantidad de columnas de la matriz A
mA = Matriz(f1, c1)

print("Matriz 1:")    # Imprimir matriz A
for fila in mA:
    print(fila)

f2 = int(input("Ingrese el número de filas de la matriz B:    ")) #se ingresa por parte del usuario la cantidad de filas de la matriz B
c2 = int(input("Ingrese el número de columnas de la matriz B: ")) #se ingresa por parte del usuario la cantidad de columnas de la matriz B
mB = Matriz(f2, c2)

print("Matriz 2:")    # Imprimir matriz B
for fila in mB:
    print(fila)

if c1 != f2:
    print("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz. No se pueden multiplicar las matrices.")
else:
    resultado = multiplicar(mA, mB)     #se multiplican las matrices
    print("La matriz resultado de la multiplicación es: ")  #imprimir el resultado de la multiplicacion de matrices
    for fila in resultado:
        print(fila)