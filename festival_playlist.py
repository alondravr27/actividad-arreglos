nombres = []
artistas = []
duraciones = []
popularidades = []


def agregar_canciones():
    cantidad = int(input("\n¿Cuantas canciones deseas agregar?: "))

    for i in range(cantidad):
        print(f"\n--- Cancion {i + 1} ---")

        nombre = input("Nombre de la cancion: ")
        artista = input("Nombre del artista: ")
        duracion = float(input("Duracion en minutos: "))

        popularidad = int(input("Ingrese la popularidad (1-100): "))

        while popularidad < 1 or popularidad > 100:
            print("Error: la popularidad debe estar entre 1 y 100.")
            popularidad = int(input("Ingrese de nuevo el valor: "))

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print("\nCanciones agregadas correctamente")


def ver_reportes():
    if len(nombres) == 0:
        print("\nNo hay canciones registradas.")
        return

    total_canciones = len(nombres)
    duracion_total = sum(duraciones)
    promedio = sum(popularidades) / total_canciones

    indice_mayor = popularidades.index(max(popularidades))
    indice_menor = popularidades.index(min(popularidades))

    print("\n========== REPORTES ==========")
    print("Total de canciones:", total_canciones)
    print("Duración total:", round(duracion_total, 2), "minutos")

    print("\nCancion más popular:")
    print(nombres[indice_mayor], "-", artistas[indice_mayor])
    print("Popularidad:", popularidades[indice_mayor])

    print("\nCancion menos popular:")
    print(nombres[indice_menor], "-", artistas[indice_menor])
    print("Popularidad:", popularidades[indice_menor])

    print("\nPromedio de popularidad:", round(promedio, 2))


def buscar_canciones():
    if len(nombres) == 0:
        print("\nNo hay canciones registradas.")
        return

    print("\n===== BUSCAR CANCIONES =====")
    print("1. Buscar por artista")
    print("2. Buscar popularidad")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        artista_buscar = input("Ingresa el nombre del artista: ").lower()

        encontrado = False

        for i in range(len(nombres)):
            if artista_buscar in artistas[i].lower():
                print("\nCancion:", nombres[i])
                print("Artista:", artistas[i])
                print("Duracion:", duraciones[i], "minutos")
                print("Popularidad:", popularidades[i])
                encontrado = True

        if not encontrado:
            print("\nNo hay canciones de ese artista.")

    elif opcion == "2":
        minimo = int(input("Popularidad minima: "))
        maximo = int(input("Popularidad maxima: "))

        encontrado = False

        for i in range(len(nombres)):
            if minimo <= popularidades[i] <= maximo:
                print("\nCancion:", nombres[i])
                print("Artista:", artistas[i])
                print("Duracion:", duraciones[i], "minutos")
                print("Popularidad:", popularidades[i])
                encontrado = True

        if not encontrado:
            print("\nNo hay canciones en ese rango")

    else:
        print("\nOpcion no valida")


def playlist_recomendada():
    if len(nombres) == 0:
        print("\nNo hay canciones registradas")
        return

    promedio = sum(popularidades) / len(popularidades)

    print("\n====== PLAYLIST RECOMENDADA ======")
    print("Promedio de popularidad:", round(promedio, 2))
    print("\nCanciones con popularidad superior al promedio:\n")

    encontrado = False

    for i in range(len(nombres)):
        if popularidades[i] > promedio:
            print("--------------------------")
            print("Cancion:", nombres[i])
            print("Artista:", artistas[i])
            print("Duracion:", duraciones[i], "minutos")
            print("Popularidad:", popularidades[i])
            encontrado = True

    if not encontrado:
        print("No hay canciones que superen el promedio")


def menu():
    while True:
        print("\n================================")
        print("      FESTIVAL PLAYLIST")
        print("================================")
        print("1. Agregar canciones")
        print("2. Ver reportes")
        print("3. Buscar canciones")
        print("4. Playlist recomendada")
        print("5. Salir")
        print("================================")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_canciones()

        elif opcion == "2":
            ver_reportes()

        elif opcion == "3":
            buscar_canciones()

        elif opcion == "4":
            playlist_recomendada()

        elif opcion == "5":
            print("\nSaliendo...")
            break

        else:
            print("\nOpcion no valida")


menu()
