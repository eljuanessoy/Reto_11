import random #importamos la funcion random

def Matriz(fil, colum):  #funcion que almacena los valores ingresados para la matriz
    matriz = []
    for i in range(fil):
        fila = []
        for n in range(colum):
            fila.append(random.randint(1, 100))
        matriz.append(fila)
    return matriz

def suma_columna(matriz, NumColumna): #funcion que suma los valores de la columna seleccionada
  suma = 0
  for fila in matriz:
    suma += fila[NumColumna]
  return suma

if __name__ == "__main__":
    f = int(input("Ingrese el número de filas de la matriz: ")) #se ingresa por parte del usuario la cantidad de filas de la matriz
    c = int(input("Ingrese el número de columnas de la matriz: ")) #se ingresa por parte del usuario la cantidad de columnas de la matriz
    matriz = Matriz(f, c)
    print()
    print("Matriz ingresada: ") #se imprime la matriz ingresada             
    for fila in matriz:
      print(fila)
    print()

if __name__ == "__main__":
   NumColumna = int(input("Ingrese el número de la columna que va a sumar (No olvide que la primera columna es cero): ")) #seleccionamos el numero de columna que se sumara
   SumaColumna = suma_columna(matriz, NumColumna) #ingresamos los datos a la funcion
   print()
   print(f"La suma de los elementos de la columna {NumColumna} es: ") #imprimimos el resultado de los datos ingresados
   print(SumaColumna)