# Declaración del diccionario de las estaciones de la línea 2 de Guadalajara
estaciones_D = {'Arcos De Zapopan':0, 'Periférico Belenes': 30, 'Mercado Del Mar':45, 'Zapopan Centro':65, 'Plaza Patria':70, 'Circunvalación Country':80, 'Ávila Camacho':90, 'Normal':100, 'Santuario':120, 'Plaza Universidad': 140, 'Independencia':150, 'Plaza De La Bandera': 160, 'CUCEI': 170, 'Revolución': 180, 'Río Nilo': 190, 'Tlaquepaque Centro': 200, 'Lázaro Cárdenas': 210, 'Central De Autobuses': 220}
# ------------- CONSTANTES --------------
# Velocidad promedio del metro en km/h
VELOCIDAD = 70
# Unidad de tiempo en minutos
TIEMPO_ESPERA = 3
print("-"*90)

# -----------------------Funciones de datos esenciales--------------------------
# Cálculo de distancias
def distancias(actual_estacion, final_estacion):
    return abs(final_estacion - actual_estacion)
# Cálculo de tiempo en minutos
def tiempo(distancia, velocidad):
    t = distancia/velocidad
    return t*60
# Obtener posiciones de la estación determinada
def index(estacion):
    contador = 0
    for station in estaciones_D:
        contador += 1
        if estacion == station:
            return contador
# Obtener los costos por terminal considerando las tarifas:
def costos_tarifas(num_estaciones):
    costos = 0.0
    for tarifa in range(1, num_estaciones + 1):
        costos += float(input(f'Ingresa el costo de la terminal {tarifa}: '))
    return costos
# Limpiar la información a un tipo title o upper
def limpiar(data):
    if data != 'cucei':
        data = data.title()
    else:
        data = data.upper()
    return data

# ----------------------Programa principal --------------------------------------
while True:
    # Recorrer las keys (estaciones) del diccionario
    print("Línea 2:")
    for estacion in estaciones_D.keys():
        print(estacion)
    # Estación actual del viajero
    print("De las estaciones que aparecen en la línea 2:\n")
    actual_estacion = input("¿Cúal es tu estación actual?: ").lower()

    # Limpiar la información de estación inicial
    actual_estacion = limpiar(actual_estacion)

    # Verificación de estación actual en el diccionario
    if actual_estacion in estaciones_D.keys():
        # Estación de llegada del viajero
        final_estacion = input("¿Cuál es la estación de destino?: ").lower()
                
        # Limpiar la información de estación final
        final_estacion = limpiar(final_estacion)
                
        # Verificación de estación final
        if final_estacion in estaciones_D.keys():
                
            # Cálcular el número de estaciones
            num_estaciones = abs(index(final_estacion) - index(actual_estacion))
                    
            # Cálculo de los costos totales:
            costos = costos_tarifas(num_estaciones)
                
            # Cálcular las distancias
            distancia = distancias(estaciones_D[actual_estacion], estaciones_D[final_estacion])
                    
            # Cálculo de tiempo total:
            tiempo_total = tiempo(distancia, VELOCIDAD) + (TIEMPO_ESPERA*num_estaciones)

            # Imprimir los resultados finales
            print('~'*95)

            print(f'El tiempo total para recorrer la estación actual ({actual_estacion}) a la estación final ({final_estacion}) es de: {tiempo_total} minutos')

            print('~'*95)

            print(f'El costo total del transporte público desde la estación actual ({actual_estacion}) hasta la estación final ({final_estacion}) es: ${costos}')

            print('~'*95)

            pregunta = input("¿Deseas seguir calculando tiempos y costos? (Si o No): ").lower()
            if pregunta == 'no':
                break
        else:
            print("La estación de llegada no existe vuelve a ingresarla")
    else:
        print("La estación actual no existe vuelve a verificar")
