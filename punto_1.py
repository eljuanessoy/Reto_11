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