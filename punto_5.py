def matriz(fil, colum): #funcion que almacena los valores ingresados para la matriz
    m = [] 
    for i in range(fil):
       fila =[] #almacenamos los elementos con el ciclo for
       for j in range(colum):
           n = int(input(f"Ingrese un número [{i}][{j}]: ")) 
           fila.append(n) 
       m.append(fila) 
    return m
    
    
def suma(mA:list, fil:int) -> float: #las entradas de la función son una lista y un entero y retorna un flotante
    SFila= sum(mA[fil-1]) #suma de los elementos de la columna dada
    return SFila


if __name__ == "__main__":
    f = int(input("Ingrese el número de filas de la matriz: ")) #se ingresa por parte del usuario la cantidad de filas de la matriz
    c = int(input("Ingrese el número de columnas de la matriz: ")) #se ingresa por parte del usuario la cantidad de columans de la matriz
    Sfil = int(input("Ingrese la fila a sumar: ")) #se escoge lafila que se sumara
    mA= matriz(f, c) #introducimos los datos a la funcion
    print ("Matriz ingresada: ") #imprimimos la matriz ingresada
    for i in range(len(mA)):
        print(mA[i])
        
    SFila = suma(mA, Sfil)
    print(f"La suma de los elementos de la fila {Sfil} es: ") #imprimimos el resultado de la suma
    print(SFila)