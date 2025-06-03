# -----------------------------
# Función que muestra el menú de opciones completo al usuario
def mostrar_menu():
    print("1-Cargar participantes")
    print("2-Cargar puntuaciones")
    print("3-Mostrar puntuaciones")
    print("4-Participantes con promedio mayor a 4")
    print("5-Participantes con promedio mayor a 7")
    print("6-Promedio de cada jurado")
    print("7-Jurado más estricto")
    print("8-Buscar participante por nombre")
    print("9-Top 3 mejores promedios")
    print("10-Mostrar participantes ordenadamente (A-Z)")
    print("11-Salir")

# -----------------------------
# Función que muestra un menú al usuario y valida que la opción ingresada
# sea un número entero entre 1 y 10.
def pedir_opcion_menu():
    while True:  # Bucle que se repite hasta que se ingrese una opción válida
        entrada = input("\nElija su opcion:")  # Solicita la opción al usuario (como texto)

        # Verifica que la entrada no esté vacía
        es_numero = entrada != ""

        # Recorre cada carácter de la entrada para asegurarse de que todos sean dígitos
        for caracter in entrada:
            if caracter < "0" or caracter > "9":
                es_numero = False  # Si algún carácter no es número, no es válido
                break  # Sale del for al encontrar un carácter no numérico

        if es_numero:
            opcion = int(entrada)  # Convierte la entrada a número entero
            if 1 <= opcion <= 11:  # Verifica que esté en el rango permitido
                return opcion  # Devuelve la opción válida y finaliza la función

        # Si no se cumple todo lo anterior, se muestra un mensaje de error
        print("Error ingrese una opcion valida")


# -----------------------------
# Función que permite cargar hasta 5 nombres válidos de participantes.
# Devuelve una lista con los nombres ingresados.
def cargar_participantes() -> list:
    Participantes = []
    while len(Participantes) < 5:
        nombre = input("Ingrese el nombre de los participantes: ")
        if validar_nombre(nombre):
            Participantes += [nombre]
        else:
            print("Nombre invalido ,debe tener al menos 3 caracteres y solo letras")
    return Participantes


# -----------------------------
# Función que valida que el nombre ingresado tenga al menos 3 letras y solo contenga letras y espacios.
def validar_nombre(nombre: str) -> bool:
    if len(nombre) < 3:
        return False
    for i in nombre.lower():
        if not (("a" <= i <= "z") or i == " "):
            return False
    return True


# -----------------------------
# Función que muestra por pantalla la lista de participantes ingresados, numerados.
def mostrar_nombres(Participantes):
    print("Participantes ingresados: ")
    i = 1
    for nombre in Participantes:
        print(f"{i}- {nombre}")
        i += 1


# -----------------------------
# Función que permite ingresar las notas que cada jurado le da a cada participante.
# Devuelve una matriz (lista de listas) con las puntuaciones validadas.
def cargar_puntuaciones(cantidad_participantes, cantidad_jurados):
    matriz = []  # Esta lista va a contener las filas de notas (una por participante)

    for i in range(cantidad_participantes):  # Itera por cada participante
        fila = []  # Lista temporal para almacenar las notas de un participante

        for j in range(cantidad_jurados):  # Itera por cada jurado
            while True:  # Bucle que insiste hasta que se ingrese una nota válida
                # Pide al usuario la nota del jurado j+1 para el participante i+1
                entrada = input(f"Ingrese la nota del jurado {j+1} para el participante {i+1}: ")

                # Supone que la entrada es válida hasta que se demuestre lo contrario
                es_numero = True

                # Verifica que todos los caracteres de la entrada sean dígitos
                for caracter in entrada:
                    if caracter < "0" or caracter > "9":
                        es_numero = False  # Si encuentra algo que no es número, se invalida
                        break

                # Si es un número y no está vacío
                if es_numero and entrada != "":
                    nota = int(entrada)  # Convierte la entrada en un número entero

                    # Verifica que la nota esté en el rango válido (1 a 10)
                    if validar_ingreso_nota(nota):
                        fila += [nota]  # Agrega la nota válida a la fila del participante
                        break  # Sale del bucle while para pasar al siguiente jurado
                    else:
                        print(" La nota debe estar entre 1 y 10")  # Mensaje de error si está fuera de rango
                else:
                    print("Entrada inválida. Ingrese solo números enteros")  # Si no era un número válido

        matriz += [fila]  # Agrega la fila completa (notas del participante) a la matriz principal

    return matriz  # Devuelve la matriz de puntuaciones una vez finalizada la carga


# -----------------------------
# Función que valida que una nota esté en el rango de 1 a 10.
def validar_ingreso_nota(nota: int) -> bool:
    if nota < 1 or nota > 10:
        return False
    return True


# -----------------------------
# Función que muestra los puntajes dados por los jurados a cada participante,
# y calcula su promedio usando la función calcular_promedio.
def mostrar_puntuaciones(matriz, participantes):
    for i in range(len(matriz)):
        print(f"Nombre del Participante: {participantes[i]}")
        fila = matriz[i]
        for j in range(len(fila)):
            print(f"Puntaje del jurado {j+1}: {fila[j]}")
        promedio = calcular_promedio(fila)
        print(f"PUNTAJE PROMEDIO: {promedio}\n")


# -----------------------------
# Función genérica que calcula y devuelve el promedio de una lista de números.
def calcular_promedio(lista):
    return sum(lista) / len(lista) if len(lista) > 0 else 0


# -----------------------------
# Función que muestra los participantes cuyo promedio de puntaje es mayor
# al mínimo recibido por parámetro. Si no hay ninguno, muestra mensaje de error.
def mostrar_promedios_mayores(puntuaciones, participantes, minimo):
    bandera = False
    for i in range(len(puntuaciones)):
        promedio = calcular_promedio(puntuaciones[i])
        if promedio > minimo:
            print(f"{participantes[i]}: - Promedio: {promedio}\n")
            bandera = True
    if not bandera:
        print(f"\nError: No hay participantes con promedio mayor a {minimo}\n")


# -----------------------------
# Función que muestra el promedio otorgado por cada jurado.
# Recorre la matriz por columnas y usa calcular_promedio.
def promedio_por_jurado(matriz):
    if not matriz:
        print("Error no hay puntuacion cargada")
        return

    cantidad_jurados = len(matriz[0])
    cantidad_participantes = len(matriz)

    for j in range(cantidad_jurados):
        suma = 0
        for i in range(cantidad_participantes):
            suma += matriz[i][j]
        promedio = suma / cantidad_participantes
        print(f"\nEl promedio del jurado {j+1}: {promedio}")



# -----------------------------
# Función que determina cuál jurado fue el más estricto,
# es decir, el que otorgó el promedio de notas más bajo.
def jurado_mas_estricto(matriz):
    # Verifica si la matriz está vacía (no se cargaron puntuaciones)
    if not matriz:
        print("Error: No hay puntuaciones cargadas.")
        return  # Termina la función si no hay datos

    # Calcula la cantidad de jurados (columnas) y participantes (filas)
    cantidad_jurados = len(matriz[0])  # Se asume que todas las filas tienen misma longitud
    cantidad_participantes = len(matriz)

    # Inicializa el promedio más bajo y el índice del jurado más estricto
    promedio_minimo = None
    jurado_mas_estricto = -1

    # Recorre cada jurado (columna por columna)
    for j in range(cantidad_jurados):
        # Obtiene las notas que ese jurado dio a todos los participantes
        notas_jurado = [matriz[i][j] for i in range(cantidad_participantes)]

        # Calcula el promedio de ese jurado
        promedio = calcular_promedio(notas_jurado)

        # Compara para ver si este promedio es el más bajo hasta ahora
        if promedio_minimo is None or promedio < promedio_minimo:
            promedio_minimo = promedio  # Guarda el nuevo promedio más bajo
            jurado_mas_estricto = j     # Guarda el índice del jurado más estricto

    # Muestra el jurado más estricto (se suma 1 porque el índice empieza en 0)
    print(f"El jurado más estricto fue el jurado {jurado_mas_estricto + 1} con  promedio de {promedio_minimo}\n")


# -----------------------------
# Función que permite buscar un participante por nombre (sin importar mayúsculas).
# Si lo encuentra, muestra sus puntajes y promedio. Si no, muestra error.
def buscar_participante_por_nombre(participantes, puntuaciones):
    nombre_ingresado = input("Ingrese el nombre del participante a buscar: ").lower()

    for i in range(len(participantes)):
        if participantes[i].lower() == nombre_ingresado:
            print(f"\nParticipante encontrado: {participantes[i]}")
            for j in range(len(puntuaciones[i])):
                print(f"Puntaje del jurado {j+1}: {puntuaciones[i][j]}")
            promedio = calcular_promedio(puntuaciones[i])
            print(f"Promedio: {promedio}\n")
            return

    print("Error participante no encontrado.\n")


# -----------------------------
# Función que muestra los 3 participantes con mayor puntaje promedio.
# No usa listas ni sort, solo variables auxiliares para determinar los 3 mejores.
def mostrar_top_3_participantes(participantes, puntuaciones):
    # Inicializa los 3 mejores promedios encontrados (con valores imposibles bajos)
    mejor1 = -1
    mejor2 = -1
    mejor3 = -1

    # Inicializa los nombres correspondientes a esos 3 mejores promedios
    nombre1 = ""
    nombre2 = ""
    nombre3 = ""

    # Recorre todos los participantes
    for i in range(len(participantes)):
        nombre = participantes[i]  # Nombre del participante actual
        promedio = calcular_promedio(puntuaciones[i])  # Calcula su promedio

        # Si el promedio es mayor que el mejor1, se reordenan todos (suben 1 lugar)
        if promedio > mejor1:
            mejor3 = mejor2
            nombre3 = nombre2

            mejor2 = mejor1
            nombre2 = nombre1

            mejor1 = promedio
            nombre1 = nombre

        # Si no es el mejor, pero sí mejor que el segundo
        elif promedio > mejor2:
            mejor3 = mejor2
            nombre3 = nombre2

            mejor2 = promedio
            nombre2 = nombre

        # Si no es mejor que el primero ni el segundo, pero sí mejor que el tercero
        elif promedio > mejor3:
            mejor3 = promedio
            nombre3 = nombre

    # Muestra el top 3 final
    print("\nLos 3 participantes con mayor puntaje promedio son: ")
    print(f"1- {nombre1} - Promedio: {mejor1}")
    print(f"2- {nombre2} - Promedio: {mejor2}")
    print(f"3- {nombre3} - Promedio: {mejor3}\n")



# -----------------------------
# Función que valida que las listas de nombres y puntuaciones no estén vacías.
# Se usa en el menú para evitar ejecutar opciones si no hay datos cargados.
def validar_datos(nombres, puntuaciones):
    if not nombres or not puntuaciones:
        print("Primero debe cargar participantes y puntuaciones\n")
        return False
    return True

# -----------------------------
# Función que muestra los participantes ordenados alfabéticamente (sin importar mayúsculas),
# junto con sus puntajes y promedios correspondientes.
def mostrar_participantes_ordenados(participantes, puntuaciones):
    cantidad = len(participantes)  # Cantidad total de participantes

    # Crear copias de las listas originales para no modificar los datos reales
    nombres_ordenados = participantes[:]
    notas_ordenadas = puntuaciones[:]

    # Ordenamiento tipo burbuja: compara los nombres y los intercambia si están fuera de orden
    for i in range(cantidad - 1):
        for j in range(i + 1, cantidad):
            # Comparar los nombres ignorando mayúsculas
            if nombres_ordenados[i].lower() > nombres_ordenados[j].lower():
                # Intercambiar nombres
                aux_nombre = nombres_ordenados[i]
                nombres_ordenados[i] = nombres_ordenados[j]
                nombres_ordenados[j] = aux_nombre

                # Intercambiar las puntuaciones del mismo modo, para mantener la correspondencia
                aux_notas = notas_ordenadas[i]
                notas_ordenadas[i] = notas_ordenadas[j]
                notas_ordenadas[j] = aux_notas

    # Mostrar los participantes ya ordenados alfabéticamente
    print("\nParticipantes ordenados alfabéticamente:\n")
    for i in range(cantidad):
        print(f"{i+1}. {nombres_ordenados[i]}")  # Mostrar nombre con número
        for j in range(len(notas_ordenadas[i])):  # Mostrar las notas de cada jurado
            print(f"   Puntaje jurado {j+1}: {notas_ordenadas[i][j]}")
        promedio = calcular_promedio(notas_ordenadas[i])  # Calcular promedio del participante
        print(f"   Promedio: {promedio:.2f}\n")  # Mostrar el promedio con 2 decimales
