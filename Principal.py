import os # manejo de cmd

print("ESTRUCTURA DE DATOS B")
print("\nBYRON GERARDO CASTILLO GÓMEZ 201700544")


def mostrar_menu():
    print("\nMENÚ DE MAPEO LEXICOGRÁFICO:")
    print("1.Mapeo por Filas.")
    print("2.Mapeo por Columnas.")
    print("3.Salir.")

def generar_matriz_evaluadora(filas , columnas):
    matriz_evaluadora = []
    asignador = 0
    for generador in range(0, filas):
        matriz_evaluadora.append([0]*columnas)
    for fila in range(0, filas):
        for columna in range(0, columnas):
            matriz_evaluadora[fila][columna] = str(asignador)
            asignador = asignador + 1
    return matriz_evaluadora

def graficar_por_mapeo_en_filas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for fila in range(0, filas):
        for columna in range(0, columnas):
            print(matriz[fila][columna])

def graficar_por_mapeo_en_columnas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    for columna in range(0, columnas):
        for fila in range(0, filas):
            print(matriz[fila][columna])

def graficar_matriz(matriz):
    inicio = "digraph{ rankdir=LR; "
    parametros_nodo_generales = "node [shape=record,width=5,height=.5, fillcolor=darkseagreen4, style=filled]; nodesep=0.02; "
    estructura = ""
    final = "}"
    filas = len(matriz)
    columnas = len(matriz[0])
    for fila in range(0, filas):
        generador = "node" + str(fila) + "[label = \"{"
        for columna in range(0, columnas):
            #print(matriz[fila][columna])
            generador = generador + str(matriz[((filas-1)-fila)][columna])
            if(columna != (columnas-1)):
               generador = generador +"|"
        generador = generador + "}\"]; "
        estructura = estructura + generador
    return ( inicio + parametros_nodo_generales + estructura + final)



def devolver_posicion_mapeo_fila(matriz, posicion_fila, posicion_columna):
    return  ((posicion_fila*(len(matriz[0]))) + posicion_columna)

def devolver_posicion_mapeo_col(matriz, posicion_fila, posicion_columna):
    return  ((posicion_columna*(len(matriz))) + posicion_fila)

def generar_archivo():
        try:
         nombre_archivo_graficador = "grafico_de_mapeo.gv"
         #print("contenido generado: " + str(graficar_matriz()))
         archivo_graphviz = open(nombre_archivo_graficador ,"w")
         archivo_graphviz.write(str(graficar_matriz(matriz_generada)))
         archivo_graphviz.close()
        except:
            print("Se produjo un error al generar el archivo graficador")

def graficar_estructura():
        try:
            #os.system("cd \ ") os.system("cd Program Files (x86)\Graphviz 2.28"+"\\"+"bin") no es necesario acceder a la ubicación del dot.exe de graphviz
            generar_archivo()
            comando_transformador = "dot.exe -Tjpg grafico_de_mapeo.gv " + "-o  imagen_matriz.jpg"
            os.system(comando_transformador)
            #print(str(os.getcwd()))
            os.system("imagen_matriz.jpg")
        except:
         print("No se pudo graficar la estructura y mostrarla")




while True:
    mostrar_menu()
    opcion = input("Elija una opción del menú:")
    try:
     seleccion = int(opcion)
     if seleccion <= 0 or seleccion > 3:
         print("La opción elegida no se encuentra dentro de las opciones establecidas.")
     elif seleccion == 1:
         try:
             print("Por favor indique la dimensión de la matriz: ")
             filas_matriz = int(input("No. Filas: "))
             columnas_matriz = int(input("No. Columnas: "))
             if filas_matriz > 0 and columnas_matriz > 0:
                matriz_generada = generar_matriz_evaluadora(filas_matriz, columnas_matriz)
                print(matriz_generada)
                try:
                    print("Ingrese la posición a linealizar: ")
                    posicion_fi = int(input("FILA:"))
                    posicion_col = int(input("COLUMNA:"))
                    if(posicion_fi >= 0 and  posicion_fi < (len(matriz_generada))) and (posicion_col >= 0 and posicion_col< (len(matriz_generada[0]))):
                        print("La posición mapeada por fila es: "+ str(devolver_posicion_mapeo_fila(matriz_generada, posicion_fi, posicion_col)))
                        print("MAPEO EN FILAS:")
                        graficar_por_mapeo_en_filas(matriz_generada)
                        graficar_estructura()
                    else:
                        print("la posición indicada no existe en la matriz")
                except:
                    print("la posicion indicada no es válida: ")
                devolver_posicion_mapeo_fila(matriz_generada, posicion_fi, posicion_col)
             else:
                 print("0 y/o números negativos no son una dimensión válida")
         except:
             print("la dimensión colocada no es válida")
     elif seleccion == 2:
         try:
             print("Por favor indique la dimensión de la matriz: ")
             filas_matriz = int(input("No. Filas: "))
             columnas_matriz = int(input("No. Columnas: "))
             if filas_matriz > 0 and columnas_matriz > 0:
                 matriz_generada = generar_matriz_evaluadora(filas_matriz, columnas_matriz)
                 print(matriz_generada)
                 try:
                     print("Ingrese la posición a linealizar: ")
                     posicion_fi = int(input("FILA:"))
                     posicion_col = int(input("COLUMNA:"))
                     if (posicion_fi >= 0 and posicion_fi < (len(matriz_generada))) and (posicion_col >= 0 and posicion_col < (len(matriz_generada[0]))):
                         print("La posición mapeada por fila es: " + str(devolver_posicion_mapeo_col(matriz_generada, posicion_fi, posicion_col)))
                         print("MAPEO EN COLUMNAS:")
                         graficar_por_mapeo_en_columnas(matriz_generada)
                         graficar_estructura()
                     else:
                         print("la posición indicada no existe en la matriz")
                 except:
                     print("la posicion indicada no es válida: ")
             else:
                 print("0 y/o números negativos no son una dimensión válida")
         except:
             print("la dimensión colocada no es válida")
     else:
         print("EJECUCIÓN FINALIZADA")
         break
    except ValueError as errorOpcion:
        print("El dato ingresado no es válido dentro del menú.")