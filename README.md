# Reto #11 😲
By Juan Esteban Molina Rey (eljuanessoy)

### 1. Desarrolle un programa que permita realizar la [suma/resta de matrices](https://es.wikipedia.org/wiki/Adici%C3%B3n_matricial). El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
def Matriz(fil,colum):  #se definene las variables de la funcion
  matriz = [] #se almacenan los elementos de la matriz en una lista vacia
  for i in range(fil):
    filas =[] #lista vacia con el ciclo for
    for j in range(colum):
        n = int(input(f"Ingrese un número [{i}][{j}]: ")) #aqui se ubican los elementos ingresados en la matriz
        filas.append(n) #se agregan los elementos de las filas
    matriz.append(filas) #va almacenando los datos en la matriz
  return matriz

def Suma(A, B):
  suma = [] #se almacenan los elementos de la suma de matrices
  for i in range(len(A)): #toma cada uno de los elementos de las filas de las matrices
    m = []
    for j in range(len(A[0])): #toma cada uno de los elementos de las columnas de las matrices
      m.append(A[i][j] + B[i][j]) #realiza la suma de los elementos en ambas matrices
        
    suma.append(m) #los resultados de la suma se agregan a la matriz
  return suma

def Resta(A, B):
  rest = [] #se almacenan los elementos de la resta de matrices
  for i in range(len(A)): #toma cada uno de los elementos de las filas de las matrices
    m = []
    for j in range(len(A[0])): #toma cada uno de los elementos de las columnas de las matrices
      m.append(A[i][j] - B[i][j]) #realiza la resta de los elementos en ambas matrices

    rest.append(m) #los resultados de la resta se agregan a la matriz
  return rest
      
  

if __name__ == "__main__":  
  fil = int(input("Ingrese la cantidad de filas: ")) #se ingresa la cantidad de filas
  colum = int(input("Ingrese la cantidad de columnas: ")) #se ingresa la cantidad de columnas
  mA = Matriz(fil,colum) #se evalúa la función para formar la matriz A
  print()
  print("Matriz A: ")
  for i in range(len(mA)):
    print(mA[i])
  mB = Matriz(fil,colum) #se evalúa la función para formar la matriz B
  print()
  print("Matriz B: ")
  for i in range(len(mB)):
    print(mB[i]) 
  if len(mA) == len(mB) and len(mA[0]) == len(mB[0]): #se verifica que ambas matrices tengan el mismo número de filas y columnas
    suma = Suma(mA, mB) #se evalúa la función para sumar las matrices
    rest = Resta(mA, mB) #se evalúa la función para restar las matrices
    print()
    print("La suma y resta de las matrices es posible")
    print("El resultado de la suma de las matrices es: ") #imprimimos los resultados
    for i in range(len(suma)):
      print(suma[i])
    print("El resultado de la resta de las matrices es: ")
    for i in range(len(rest)):
      print(rest[i])
  else:
    print("Ni la suma ni la resta de las matrices es posible")
```

2. Desarrolle un programa que permita realizar el [producto de matrices](https://es.wikipedia.org/wiki/Multiplicaci%C3%B3n_de_matrices). El programa debe validar las condiciones necesarias para ejecutar la operación.

```python
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
```

3. Desarrolle un programa que permita obtener la  [matriz transpuesta](https://es.wikipedia.org/wiki/Matriz_transpuesta) de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.

```python

```

4. Desarrollar un programa que sume los elementos de una columna dada de una matriz.

```python

```

5. Desarrollar un programa que sume los elementos de una fila dada de
una matriz.

```python

```
