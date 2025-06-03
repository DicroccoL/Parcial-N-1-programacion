import os
from funciones import *  # Importa todas las funciones definidas en el archivo funciones.py

# Inicializa las listas que almacenarán los nombres y las puntuaciones
ejecutar_nombres = []
ejecutar_puntuaciones = []

# Bucle principal del menú
while True:
    # Muestra las opciones del menú al usuario
    mostrar_menu()
    # Solicita al usuario una opción del menú y la valida
    opcion = pedir_opcion_menu()

    # Opción 1: Cargar participantes
    if opcion == 1:
        print("Cargando participantes...")
        ejecutar_nombres = cargar_participantes()  # Guarda los nombres cargados
        mostrar_nombres(ejecutar_nombres)  # Muestra los nombres ingresados

    # Opción 2: Cargar puntuaciones de 3 jurados a 5 participantes
    elif opcion == 2:
        print("Cargando puntuaciones...")
        ejecutar_puntuaciones = cargar_puntuaciones(5, 3)

    # Opción 3: Mostrar todas las puntuaciones con su promedio por participante
    elif opcion == 3:
        if validar_datos(ejecutar_nombres, ejecutar_puntuaciones):
            print("Mostrando puntuaciones...")
            mostrar_puntuaciones(ejecutar_puntuaciones, ejecutar_nombres)

    # Opción 4: Mostrar participantes con promedio mayor a 4
    elif opcion == 4:
        if validar_datos(ejecutar_nombres, ejecutar_puntuaciones):
            mostrar_promedios_mayores(ejecutar_puntuaciones, ejecutar_nombres, 4)

    # Opción 5: Mostrar participantes con promedio mayor a 7
    elif opcion == 5:
        if validar_datos(ejecutar_nombres, ejecutar_puntuaciones):
            mostrar_promedios_mayores(ejecutar_puntuaciones, ejecutar_nombres, 7)

    # Opción 6: Mostrar promedio de cada jurado
    elif opcion == 6:
        if validar_datos(ejecutar_nombres, ejecutar_puntuaciones):
            promedio_por_jurado(ejecutar_puntuaciones)

    # Opción 7: Determinar el jurado más estricto (menor promedio)
    elif opcion == 7:
        if validar_datos(ejecutar_nombres, ejecutar_puntuaciones):
            jurado_mas_estricto(ejecutar_puntuaciones)

    # Opción 8: Buscar un participante por su nombre
    elif opcion == 8:
        if validar_datos(ejecutar_nombres, ejecutar_puntuaciones):
            buscar_participante_por_nombre(ejecutar_nombres, ejecutar_puntuaciones)

    # Opción 9: Mostrar el top 3 de promedios más altos
    elif opcion == 9:
        if validar_datos(ejecutar_nombres, ejecutar_puntuaciones):
            mostrar_top_3_participantes(ejecutar_nombres, ejecutar_puntuaciones)

    # Opción 10: Mostrar los participantes ordenados alfabéticamente
    elif opcion == 10:
        if validar_datos(ejecutar_nombres, ejecutar_puntuaciones):
            mostrar_participantes_ordenados(ejecutar_nombres, ejecutar_puntuaciones)

    # Opción 11: Salir del programa
    elif opcion == 11:
        input("\nCerrando programa....Toque un botón")
        break  # Sale del bucle y termina el programa

    # Pausa el programa hasta que el usuario presione una tecla
    input("\nToque cualquier tecla para continuar\n")
    
    # Limpia la pantalla para mostrar el menú nuevamente (solo funciona en Windows)
    os.system("cls")
