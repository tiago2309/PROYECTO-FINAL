# Importación necesaria para el cálculo de distancias y demás usos
import math
import csv
import matplotlib.pyplot as plt

def graficar_poligonal(coordenadas_corregidas, nombre_archivo="poligonal.png"):
    # Crea una nueva figura de tamaño 10x8 pulgadas para la visualización
    plt.figure(figsize=(10, 8))

    # Separa las coordenadas X y Y en dos listas diferentes
    xs = [x for x, y in coordenadas_corregidas]
    ys = [y for x, y in coordenadas_corregidas]

    # Dibuja la poligonal conectando los puntos con líneas y marcando cada vértice con un círculo
    plt.plot(xs, ys, marker='o', linestyle='-', color='blue')

    # Recorre todos los puntos para etiquetarlos y mostrar la distancia entre cada par de puntos consecutivos
    for i, (x, y) in enumerate(coordenadas_corregidas):
        # Agrega una etiqueta "P1", "P2", etc., ligeramente desplazada hacia arriba
        plt.text(x, y + 0.5, f"P{i+1}", fontsize=9, ha='center', va='bottom', color='darkred')
        
        # Si no es el primer punto, calcular y mostrar la distancia al punto anterior
        if i > 0:
            x0, y0 = coordenadas_corregidas[i - 1]  # Punto anterior
            distancia = math.hypot(x - x0, y - y0)  # Distancia euclidiana
            xm = (x + x0) / 2  # Coordenada X del punto medio
            ym = (y + y0) / 2  # Coordenada Y del punto medio
            plt.text(xm, ym, f"{distancia:.2f} m", fontsize=8, ha='center', va='center', color='black')  # Etiqueta

    # Título y etiquetas de los ejes
    plt.title("Poligonal")
    plt.xlabel("X")
    plt.ylabel("Y")

    # Habilita la cuadrícula
    plt.grid(True)

    # Asegura que los ejes X e Y tengan la misma escala
    plt.axis('equal')

    # Guarda el gráfico como archivo PNG con alta resolución
    plt.savefig(nombre_archivo, dpi=300)
    plt.close()  # Cierra la figura para liberar memoria

    # Mensaje de confirmación
    print(f"\nGráfico guardado como '{nombre_archivo}' con amor.")


def mostrar_menú(): # Esta función imprime el menú principal para que el usuario pueda interactuar
    print("╔═════════════════════════════════════════════╗")
    print("║        Bienvenido al TopograficTool         ║")
    print("╠═════════════════════════════════════════════╣")
    print("║  1. Ingresar los datos manualmente          ║")
    print("║  2. Cargar los datos desde un archivo(.csv) ║")
    print("║  3. Salir                                   ║")
    print("╚═════════════════════════════════════════════╝")

def exportar_a_csv(coordenadas):
    # Solicita al usuario el nombre del archivo CSV sin la extensión
    nombre_archivo = input("Escribe el nombre del archivo CSV (sin extensión): ").strip()
    
    # Si el usuario no escribe nada, se usa un nombre por defecto
    if not nombre_archivo:
        nombre_archivo = "coordenadas_exportadas"
    
    # Se agrega la extensión .csv al nombre del archivo
    nombre_archivo += ".csv"
    
    # Se abre (o crea) el archivo CSV en modo escritura con codificación UTF-8
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        # Se crea el objeto escritor CSV
        escritor = csv.writer(archivo)
        
        # Escribe la fila de encabezados
        escritor.writerow(["Punto", "X", "Y"])
        
        # Itera sobre las coordenadas y escribe cada punto en el archivo
        for i in range(len(coordenadas)):
            x, y = coordenadas[i]
            # Redondea las coordenadas a 3 decimales y las escribe con el nombre del punto
            escritor.writerow([f"Punto {i + 1}", f"{x:.3f}", f"{y:.3f}"])
    
    # Mensaje de confirmación para el usuario
    print(f"\nMira bb tu archivo CSV guardado con mucho cariño muak <3: {nombre_archivo}")

def solicitar_tipo_poligonal():
    # Solicita al usuario que indique si trabajará con una poligonal abierta o cerrada.
    
    while True:  # Bucle que se repite hasta que el usuario ingrese una opción válida
        print("¿Qué tipo de poligonal vas a trabajar mi rey/reina?")
        print("1. Abierta")
        print("2. Cerrada")
        tipo = input("Seleccione el tipo (1 o 2): ")

        if tipo == "1":
            return "abierta"  # Retorna "abierta" si elige la opción 1
        elif tipo == "2":
            return "cerrada"  # Retorna "cerrada" si elige la opción 2
        else:
            print("No mi rey/reina, esa es una opción inválida")  # Mensaje de error si la opción es incorrecta


def ingreso_datos():
    """
    Solicita al usuario las coordenadas iniciales y el azimut inicial
    en sistema sexagesimal. El azimut es convertido a formato decimal
    para su posterior uso en cálculos topográficos.
    
    Retorna:
        - x_inicial (float): Coordenada X del punto de inicio.
        - y_inicial (float): Coordenada Y del punto de inicio.
        - azimut_decimal (float): Azimut inicial en grados decimales.
    """
    # Mensajes informativos para el usuario
    print("\n>>> Ingreso de coordenadas y azimut inicial")
    print("RECUERDA: Ingresa los ángulos en sistema sexagesimal")
    print("          Ingrese las coordenadas del punto inicial (X, Y) en metros.")
    print("          Puede usar coordenadas reales o un sistema local arbitrario.")
    
    # Se piden las coordenadas del punto inicial
    x_inicial = float(input("Ingrese la coordenada X del punto inicial: "))
    y_inicial = float(input("Ingrese la coordenada Y del punto inicial: "))
    
    # Ingreso del azimut inicial
    print("Ingrese el azimut inicial en sistema sexagesimal:")
    
    # Validación del formato correcto de minutos y segundos
    while True:
        grados = int(input("  Grados: "))
        minutos = int(input("  Minutos: "))
        segundos = float(input("  Segundos: "))
        
        # Asegura que los minutos y segundos estén en el rango válido
        if 0 <= minutos < 60 and 0 <= segundos < 60:
            break
        else:
            print("Noporolo, otra vez, los minutos y segundos deben estar entre 0 y 59.")
    
    # Conversión del ángulo de sexagesimal a decimal
    azimut_decimal = grados + minutos / 60 + segundos / 3600
    
    # Muestra el azimut convertido para verificación
    print(f"El azimut inicial en decimal: {azimut_decimal:.3f}°")
    
    # Devuelve los valores necesarios
    return x_inicial, y_inicial, azimut_decimal

def ingresar_lados_y_angulos(poligonal_cerrada=False):
    """
    Solicita al usuario los datos de los lados de la poligonal:
    - Distancia (en metros)
    - Dirección de giro (d o i)
    - Ángulo en sistema sexagesimal (g, m, s)

    En caso de poligonal cerrada, también pregunta si los ángulos son internos o externos
    y realiza la corrección angular correspondiente.

    Retorna:
        - Una lista de tuplas con (distancia, ángulo_decimal, dirección)
        - El tipo de ángulo ('i' o 'e') si es cerrada, de lo contrario None
    """
    n = int(input("Ingresa porfa el número de lados de la poligonal: "))
    lados = []
    tipo_angulo = None
    direccion_base = None
    sum_angulos = 0

    if poligonal_cerrada:
        print("¿Los ángulos que vas a ingresar son internos (i) o externos (e)?")
        tipo_angulo = input("Escribe 'i' para internos o 'e' para externos: ").strip().lower()
        while tipo_angulo not in ['i', 'e']:
            tipo_angulo = input("Oye, debe ser 'i' (internos) o 'e' (externos): ").strip().lower()

    for i in range(n):
        print(f"\nLado {i + 1}")
        distancia = float(input("Distancia (m): "))

        if i == 0:
            direccion = input("¿El giro es hacia la izquierda (i) o derecha (d)?: ").strip().lower()
            while direccion not in ["i", "d"]:
                direccion = input("Porfa ingresa 'i' para izquierda o 'd' para derecha: ").strip().lower()
            direccion_base = direccion
        else:
            direccion = input(f"¿El giro es hacia la misma dirección ({direccion_base})?: ").strip().lower()
            while direccion != direccion_base:
                print("No bb, todos los giros deben ser iguales en esta poligonal.")
                direccion = input(f"Ingresa nuevamente '{direccion_base}': ").strip().lower()

        print("Escribe el ángulo en sistema sexagesimal:")
        while True:
            g = int(input("    Grados: "))
            m = int(input("    Minutos: "))
            s = float(input("    Segundos: "))
            if 0 <= m < 60 and 0 <= s < 60:
                break
            else:
                print("Nop, los minutos y segundos deben estar entre 0 y 59")

        angulo_decimal = g + m / 60 + s / 3600
        sum_angulos += angulo_decimal
        lados.append((distancia, angulo_decimal, direccion))

    if poligonal_cerrada:
        lados_corregidos = corregir_lados(lados, tipo_angulo)
        return lados_corregidos, tipo_angulo

    else:
        return lados, tipo_angulo

def calcular_coordenadas(x_inicial, y_inicial, azimut_inicial, lados, tipo_angulo):
    """
    Calcula las coordenadas de los puntos de una poligonal a partir de un punto inicial,
    un azimut inicial, y los lados con sus respectivos ángulos y direcciones de giro.

    Parámetros:
        x_inicial (float): Coordenada X del punto inicial.
        y_inicial (float): Coordenada Y del punto inicial.
        azimut_inicial (float): Azimut inicial en grados decimales.
        lados (list): Lista de tuplas con (distancia, ángulo, dirección de giro).
        tipo_angulo (str): 'i' para ángulos internos, 'e' para externos.

    Retorna:
        list: Lista de tuplas con las coordenadas (X, Y) de cada punto de la poligonal.
    """
        
    puntos = [(x_inicial, y_inicial)]
    azimut_actual = azimut_inicial

    for distancia, angulo, direccion in lados:
        if tipo_angulo == 'i':
            if direccion == "i":
                azimut_actual = (azimut_actual + (180 - angulo)) % 360
            else:
                azimut_actual = (azimut_actual - (180 - angulo)) % 360
        else:  # externos
            if direccion == "i":
                azimut_actual = (azimut_actual - angulo) % 360
            else:
                azimut_actual = (azimut_actual + angulo) % 360


        azimut_rad = math.radians(azimut_actual)
        x_anterior, y_anterior = puntos[-1]
        x_nuevo = x_anterior + distancia * math.sin(azimut_rad)
        y_nuevo = y_anterior + distancia * math.cos(azimut_rad)
        puntos.append((x_nuevo, y_nuevo))

    return puntos

def verificar_cierre(coordenadas, tolerancia=0.01):
    """
    Verifica si una poligonal cerrada retorna al punto inicial dentro de una tolerancia dada.

    Parámetros:
        coordenadas (list): Lista de tuplas (X, Y) con las coordenadas de los puntos.
        tolerancia (float): Tolerancia máxima permitida en metros para considerar cerrado el polígono.

    Retorna:
        bool: True si la diferencia entre el punto inicial y el final está dentro de la tolerancia, False si no.
    """
    # Se extrae la coordenada del punto inicial
    x_inicio, y_inicio = coordenadas[0]
    # Se extrae la coordenada del punto final
    x_final, y_final = coordenadas[-1]
    
    # Se calcula la diferencia absoluta en X y Y entre el inicio y el final
    dx = abs(x_inicio - x_final)
    dy = abs(y_inicio - y_final)
    
    # Se verifica si ambas diferencias están dentro de la tolerancia permitida
    if dx <= tolerancia and dy <= tolerancia:
        return True  # La poligonal se considera cerrada correctamente
    else:
        return False  # Existe un error de cierre mayor a la tolerancia


def corregir_error_cierre(coordenadas, lados):
    """
    Aplica una corrección proporcional al cierre para ajustar los errores en las coordenadas finales de una poligonal cerrada.

    Parámetros:
        coordenadas (list): Lista de tuplas (X, Y) con las coordenadas calculadas antes de corrección.
        lados (list): Lista de tuplas (distancia, ángulo, dirección) de cada lado de la poligonal.

    Retorna:
        coordenadas_corregidas (list): Lista de tuplas (X, Y) con las coordenadas ajustadas.
        error_x (float): Diferencia en X entre el punto inicial y final antes de la corrección.
        error_y (float): Diferencia en Y entre el punto inicial y final antes de la corrección.
    """
    # Coordenadas del primer y último punto
    x_inicio, y_inicio = coordenadas[0]
    x_final, y_final = coordenadas[-1]
    
    # Cálculo del error de cierre en X y Y
    error_x = x_final - x_inicio
    error_y = y_final - y_inicio

    # Suma total de las distancias recorridas (para distribuir el error proporcionalmente)
    total_lado = sum([lado[0] for lado in lados])

    # Lista para almacenar las coordenadas corregidas
    coordenadas_corregidas = [coordenadas[0]]  # El primer punto no se corrige
    acumulado = 0  # Distancia acumulada desde el punto inicial

    # Se corrigen todos los puntos desde el segundo hasta el último
    for i in range(1, len(coordenadas)):
        acumulado += lados[i - 1][0]  # Suma las distancias anteriores
        fx = (acumulado / total_lado) * error_x  # Corrección proporcional en X
        fy = (acumulado / total_lado) * error_y  # Corrección proporcional en Y
        
        # Aplicar la corrección al punto actual
        x_original, y_original = coordenadas[i]
        x_corregido = x_original + fx
        y_corregido = y_original + fy
        
        # Guardar coordenadas corregidas
        coordenadas_corregidas.append((x_corregido, y_corregido))
    
    # Retorna las coordenadas corregidas y los errores
    return coordenadas_corregidas, error_x, error_y


def corregir_lados(lados, tipo_angulo):
    """
    Aplica la corrección angular proporcional a cada ángulo medido en los lados de una poligonal cerrada.

    Parámetros:
        lados (list): Lista de tuplas (distancia, ángulo, dirección), donde 'distancia' es la longitud del lado,
                      'ángulo' es el ángulo interno/externo medido y 'dirección' es 'i' o 'd'.
        tipo_angulo (str): Indica si los ángulos son internos o externos.

    Retorna:
        list: Lista de lados con los ángulos corregidos.
    """
    n = len(lados)  # Número de lados
    # Suma de todos los ángulos ingresados por el usuario
    suma_angulos = sum([ang for _, ang, _ in lados])
    
    # Calcula la corrección por ángulo, el error angular y la suma teórica que debería tener la poligonal
    correccion, error_angular, suma_teorica = calcular_correccion_angulos(n, tipo_angulo, suma_angulos)

    # Muestra al usuario el resumen de la corrección realizada
    print("\nCorrección angular automática:")
    print(f" Suma ingresada: {suma_angulos:.3f}°")
    print(f" Teórica: {suma_teorica:.3f}°")
    print(f" Error angular: {error_angular:.3f}°")
    print(f" Corrección por ángulo: {correccion:.3f}°")

    # Se aplican las correcciones sumando el mismo valor a cada ángulo
    lados_corregidos = [(dist, ang + correccion, dir) for dist, ang, dir in lados]

    # Se retorna la nueva lista con los ángulos corregidos
    return lados_corregidos


def corregir_distancias_y_proyecciones(coordenadas, lados):
    """
    Aplica la corrección proporcional a las distancias y proyecciones de una poligonal cerrada,
    distribuyendo el error de cierre entre los puntos intermedios según la distancia acumulada.

    Parámetros:
        coordenadas (list): Lista de coordenadas (X, Y) originales de la poligonal.
        lados (list): Lista de lados, cada uno como tupla (distancia, ángulo, dirección).

    Retorna:
        list: Lista de coordenadas corregidas (X, Y).
    """
    print("\nCorrección proporcional de distancias y proyecciones")

    # Punto inicial y final de la poligonal (antes de la corrección)
    x_inicio, y_inicio = coordenadas[0]
    x_final, y_final = coordenadas[-1]

    # Cálculo del error de cierre en X y Y (diferencia entre el punto inicial y final)
    error_x = x_inicio - x_final
    error_y = y_inicio - y_final

    # Suma total de las distancias medidas en los lados
    total_distancia = sum([lado[0] for lado in lados])

    # Se inicializa la lista de coordenadas corregidas con el punto de partida
    coordenadas_corregidas = [coordenadas[0]]
    distancia_acumulada = 0  # Para llevar el acumulado de distancia desde el inicio

    # Recorre los puntos intermedios (desde el segundo hasta el último)
    for i in range(1, len(coordenadas)):
        # Acumula la distancia del lado anterior
        distancia_acumulada += lados[i - 1][0]

        # Calcula la fracción del error proporcional a la distancia acumulada
        fx = (distancia_acumulada / total_distancia) * error_x
        fy = (distancia_acumulada / total_distancia) * error_y

        # Coordenadas originales del punto actual
        x_orig, y_orig = coordenadas[i]

        # Se le aplica la corrección proporcional a las coordenadas
        x_corr = x_orig + fx
        y_corr = y_orig + fy

        # Se agregan las coordenadas corregidas a la lista
        coordenadas_corregidas.append((x_corr, y_corr))

    # Se devuelve la lista completa de coordenadas corregidas
    return coordenadas_corregidas

def calcular_suma_teorica_angulos(n: int, tipo_angulo: str) -> float:
    """
    Calcula la suma teórica de los ángulos internos o externos de una poligonal cerrada.

    Parámetros:
        n (int): Número de lados o vértices de la poligonal.
        tipo_angulo (str): Tipo de ángulo usado ('i' para internos, 'e' o cualquier otro valor para externos).

    Retorna:
        float: Suma teórica de los ángulos en grados.
    """

    # Si los ángulos son internos, la fórmula es (n - 2) * 180°
    if tipo_angulo == 'i':
        return (n - 2) * 180
    else:
        # Si los ángulos son externos, la fórmula es (n + 2) * 180°
        return (n + 2) * 180

    
def calcular_correccion_angulos(n, tipo_angulo, suma_angular_observada):
    """
    Calcula la corrección angular necesaria para distribuir proporcionalmente el error angular
    en una poligonal cerrada.

    Parámetros:
        n (int): Número de lados o vértices de la poligonal.
        tipo_angulo (str): Tipo de ángulo ('i' para internos, cualquier otro para externos).
        suma_angular_observada (float): Suma de los ángulos observados (medidos en campo).

    Retorna:
        tuple:
            - correccion (float): Corrección que debe aplicarse a cada ángulo.
            - error (float): Error angular total (teórico - observado).
            - suma_teorica (float): Suma teórica de los ángulos.
    """

    # Calcula la suma teórica según el número de lados y tipo de ángulo
    suma_teorica = calcular_suma_teorica_angulos(n, tipo_angulo)

    # Calcula el error angular como la diferencia entre la suma teórica y la observada
    error = suma_teorica - suma_angular_observada

    # La corrección que se aplicará a cada ángulo es el error dividido entre la cantidad de ángulos
    correccion = error / n

    return correccion, error, suma_teorica

    
def cargar_desde_csv():
    """
    Carga datos de una poligonal desde un archivo CSV. 
    Cada fila del archivo debe tener las columnas: 'Distancia', 'Ángulo' y 'Dirección'.

    El usuario especifica si los ángulos son internos o externos. 
    Luego, se corrige automáticamente el error angular antes de retornar los datos.

    Retorna:
        tuple:
            - lados_corregidos (list of tuples): Lista de tuplas con (distancia, ángulo corregido, dirección).
            - tipo_angulo (str): 'i' si los ángulos son internos, 'e' si son externos.
    """

    # Solicita al usuario el nombre del archivo CSV
    ruta = input("Esta bien rey/reina, ingresa el nombre del archivo CSV (con .csv): ")

    try:
        # Intenta abrir el archivo en modo lectura con codificación latin1
        with open(ruta, newline='', encoding='utf-8-sig') as archivo:
            lector = csv.DictReader(archivo)  # Usa DictReader para leer cada fila como un diccionario
            lector.fieldnames = [nombre.strip() for nombre in lector.fieldnames]
            print("Encabezados detectados:", lector.fieldnames)


            lados = []           # Lista para guardar los lados (distancia, ángulo, dirección)
            sum_angulos = 0      # Acumulador para la suma de ángulos

            for fila in lector:
                # Convierte cada valor a su tipo correspondiente y limpia la dirección
                distancia = float(fila['Distancia'.strip()])
                angulo = float(fila['Ángulo'])
                direccion = fila['Dirección'].strip().lower()

                sum_angulos += angulo  # Acumula los ángulos
                lados.append((distancia, angulo, direccion))  # Agrega el lado a la lista

            # Pide al usuario que indique si los ángulos son internos o externos
            tipo_angulo = input("¿Los ángulos son internos (i) o externos (e)? ").strip().lower()
            while tipo_angulo not in ['i', 'e']:
                tipo_angulo = input("Debe ser 'i' o 'e': ").strip().lower()

            # Se corrige automáticamente el error angular antes de retornar los datos
            n = len(lados)
            lados_corregidos = corregir_lados(lados, tipo_angulo)

            return lados_corregidos, tipo_angulo

    except FileNotFoundError:
        # Manejo si el archivo no existe
        print("bb, no encontré el archivo. Verifica el nombre y vuelve a intentarlo.")
        return None, None

    except Exception as e:
        # Manejo general de errores
        print(f"Rey/ reina hubo un error al leer el archivo: {e}")
        return None, None

    
def main():  # Función que ejecuta el menú
    while True: 
        mostrar_menú()  # Muestra las opciones del menú
        opcion = input("\nSeleccione una opcion (1-3): ")  # Solicita opción al usuario

        if opcion == "1":
            # Opción 1: Ingreso manual
            print(">>> Ingreso manual de datos")
            tipo_poligonal = solicitar_tipo_poligonal()  # Determina si es cerrada o abierta
            print(f"\nSe trabajará con una poligonal {tipo_poligonal}.")
            x_inicial, y_inicial, azimut_decimal = ingreso_datos()  # Pide coordenadas iniciales y azimut
            lados, tipo_angulo = ingresar_lados_y_angulos(poligonal_cerrada=(tipo_poligonal == "cerrada"))  # Pide los lados

            print(f"\nLISTOOO, datos iniciales registrados correctamente.")
            coordenadas = calcular_coordenadas(x_inicial, y_inicial, azimut_decimal, lados, tipo_angulo)  # Calcula coordenadas
            print("\nMira, estás son las coordenadas calculadas: ")

            i = 0
            while i < len(coordenadas):
                x, y = coordenadas[i]
                print(f"Punto {i + 1}: X = {x:.3f}, Y = {y:.3f}")  # Imprime coordenadas
                i += 1

            if tipo_poligonal == "cerrada":
                if not verificar_cierre(coordenadas, tolerancia=0.01):  # Verifica si está cerrada
                    print("La poligonal no está CERRADA bb.")
                    aplicar = input("¿Deseas aplicar corrección de cierre? (s/n): ").strip().lower()
                    if aplicar in ["sí", "si", "s"]:
                        coordenadas_corregidas, error_x, error_y = corregir_error_cierre(coordenadas, lados)
                        print(f"Error de cierre: ΔX = {error_x:.3f}, ΔY = {error_y:.3f}")

                        aplicar_distancia = input("¿Quieres aplicar también corrección proporcional en distancias y proyecciones? (s/n): ").strip().lower()
                        if aplicar_distancia in ["sí", "si", "s"]:
                            coordenadas_corregidas = corregir_distancias_y_proyecciones(coordenadas_corregidas, lados)

                        print("\nMira, acá están tus coordenadas corregidas, con mucho cariño:" )
                        i = 0
                        while i < len(coordenadas_corregidas):
                            x, y = coordenadas_corregidas[i]
                            print(f"Punto {i + 1}: X = {x:.3f}, Y = {y:.3f}")
                            i += 1

                        # Opción de guardar coordenadas corregidas
                        respuesta = input("¿Deseas guardar las coordenadas corregidas en un archivo CSV? (sí/no): ").strip().lower()
                        if respuesta in ["sí", "si", "s"]:
                            exportar_a_csv(coordenadas_corregidas)
                            print("Listo, archivo guardado :)")
                            generar = input("\n¿Deseas generar la gráfica de la poligonal? (s/n): ").strip().lower()
                            if generar == 's':
                                graficar_poligonal(coordenadas_corregidas)
                            else: 
                                print("Esta bien, no te haré la gráfica")
                        else:
                            print("Esta bien, no se guardó el archivo :(")
                    else:
                        print("Ok, no se aplicó corrección.")
                else:
                    print("Epaaa, la poligonal ya está cerrada. No se requiere corrección(menos trabajo).")
                    respuesta = input("¿Deseas guardar las coordenadas en un archivo CSV? (sí/no): ").strip().lower()
                    if respuesta in ["sí", "si", "s"]:
                        exportar_a_csv(coordenadas)
                        print("Listo, archivo guardado :)")
                        generar = input("\n¿Deseas generar la gráfica de la poligonal? (s/n): ").strip().lower()
                        if generar == 's':
                            graficar_poligonal(coordenadas)
                        else: 
                            print("Esta bien, no te haré la gráfica")
                    else:
                        print("Está bien, no se guardó el archivo :(")
            else:
                print("Amor la poligonal es abierta. No se verifica ni corrige cierre.")
                exportar = input("¿Quieres exportar estas coordenadas a CSV? (s/n): ").strip().lower()
                if exportar == "s":
                    exportar_a_csv(coordenadas)
                    print("Listo, archivo guardado :)")
                else:
                    print("Está bien, no se guardó el archivo :(")
                generar = input("\n¿Deseas generar la gráfica de la poligonal? (s/n): ").strip().lower()
                if generar == 's':
                    graficar_poligonal(coordenadas)
                else: 
                    print("Esta bien, no te haré la gráfica")

        elif opcion == "2":
            # Opción 2: Cargar datos desde CSV
            print(">>> Cargar datos desde archivo")
            tipo_poligonal = solicitar_tipo_poligonal()
            print(f"\nSe trabajará con una poligonal {tipo_poligonal}.")

            x_inicial, y_inicial, azimut_decimal = ingreso_datos()
            lados, tipo_angulo = cargar_desde_csv()

            if lados is None:
                continue  # Si hubo error al cargar CSV, reinicia menú

            coordenadas = calcular_coordenadas(x_inicial, y_inicial, azimut_decimal, lados, tipo_angulo)

            print("\nMira, estas son las coordenadas calculadas: ")
            i = 0
            while i < len(coordenadas):
                x, y = coordenadas[i]
                print(f"Punto {i + 1}: X = {x:.3f}, Y = {y:.3f}")
                i += 1

            if tipo_poligonal == "cerrada":
                if not verificar_cierre(coordenadas, tolerancia=0.01):
                    print("La poligonal no está CERRADA bb.")
                    aplicar = input("¿Deseas aplicar corrección de cierre? (s/n): ").strip().lower()
                    if aplicar in ["sí", "si", "s"]:
                        coordenadas_corregidas, error_x, error_y = corregir_error_cierre(coordenadas, lados)
                        print(f"Error de cierre: ΔX = {error_x:.3f}, ΔY = {error_y:.3f}")

                        aplicar_distancia = input("¿Quieres aplicar también corrección proporcional en distancias y proyecciones? (s/n): ").strip().lower()
                        if aplicar_distancia in ["sí", "si", "s"]:
                            coordenadas_corregidas = corregir_distancias_y_proyecciones(coordenadas_corregidas, lados)

                        print("\nMira, acá están tus coordenadas corregidas, con mucho cariño:")
                        i = 0
                        while i < len(coordenadas_corregidas):
                            x, y = coordenadas_corregidas[i]
                            print(f"Punto {i + 1}: X = {x:.3f}, Y = {y:.3f}")
                            i += 1

                        respuesta = input("¿Deseas guardar las coordenadas corregidas en un archivo CSV? (sí/no): ").strip().lower()
                        if respuesta in ["sí", "si", "s"]:
                            exportar_a_csv(coordenadas_corregidas)
                            print("Listo, archivo guardado :)")
                            generar = input("\n¿Deseas generar la gráfica de la poligonal? (s/n): ").strip().lower()
                            if generar == 's':
                                graficar_poligonal(coordenadas_corregidas)
                            else: 
                                print("Esta bien, no te haré la gráfica")
                        else:
                            print("Está bien, no se guardó el archivo :(")
                    else:
                        print("Ok, no se aplicó corrección.")
                        respuesta = input("¿Deseas guardar las coordenadas en un archivo CSV? (sí/no): ").strip().lower()
                        if respuesta in ["sí", "si", "s"]:
                            exportar_a_csv(coordenadas)
                            print("Listo, archivo guardado :)")
                            generar = input("\n¿Deseas generar la gráfica de la poligonal? (s/n): ").strip().lower()
                            if generar == 's':
                                graficar_poligonal(coordenadas)
                            else: 
                                print("Esta bien, no te haré la gráfica")
                else:
                    print("Epaaa, la poligonal ya está cerrada. No se requiere corrección (menos trabajo).")
                    respuesta = input("¿Deseas guardar las coordenadas en un archivo CSV? (sí/no): ").strip().lower()
                    if respuesta in ["sí", "si", "s"]:
                        exportar_a_csv(coordenadas)
                        print("Listo, archivo guardado :)")
                        generar = input("\n¿Deseas generar la gráfica de la poligonal? (s/n): ").strip().lower()
                        if generar == 's':
                            graficar_poligonal(coordenadas)
                        else: 
                            print("Esta bien, no te haré la gráfica")
                    else:
                        print("Está bien, no se guardó el archivo :(")
            else:
                print("Amor la poligonal es abierta. No se verifica ni corrige cierre.")
                exportar = input("¿Quieres exportar estas coordenadas a CSV? (s/n): ").strip().lower()
                if exportar == "s":
                    exportar_a_csv(coordenadas)
                    print("Listo, archivo guardado :)")
                    generar = input("\n¿Deseas generar la gráfica de la poligonal? (s/n): ").strip().lower()
                    if generar == 's':
                        graficar_poligonal(coordenadas)
                    else: 
                        print("Esta bien, no te haré la gráfica")
                else:
                    print("Está bien, no se guardó el archivo :(")

        elif opcion == "3":
            # Opción 3: Salir del programa
            print(" Gracias, nos vemos en otro poliproblema :)")
            break

        else: 
            # Si el usuario ingresa una opción inválida
            print("Ingresaste mal el número bbsote, intentalo otra vez.")


if __name__ == "__main__":
    main()