# PROYECTO-FINAL
## TopograficTool-Herramienta para cálculos topograficos en Ingenieria Civil
## Autores
- Maria Camila Palomo Avila
- Santiago Ramos Barriga
  
Curso: Programación de Computadores    
Grupo: 404 CNF (Chill Not Found)    
Universidad Nacional de Colombia  

## Problema
Durante el desarrollo del curso de Geomática Básica en Ingeniería Civil, enfrentamos múltiples retos al momento de procesar los datos topográficos obtenidos en campo. Una de las principales dificultades fue la corrección manual de errores en poligonales abiertas y cerradas, especialmente cuando los ángulos no cuadraban con los valores teóricos esperados o cuando se presentaban errores de cierre. Este proceso no solo era propenso a errores humanos, sino que también consumía tiempo valioso.

### ¿Por qué este problema?
Escogimos este problema porque lo vivimos de primera mano durante nuestras prácticas académicas. Sentimos la necesidad de contar con una herramienta que no solo automatizara el cálculo de coordenadas, sino que también permitiera realizar correcciones angulares y de cierre de manera precisa y rápida. Creemos que esta herramienta puede ser útil para otros estudiantes que necesiten validar sus datos topográficos de forma sencilla y confiable.

## Solución propuesta
Desarrollamos TopograficTool, una aplicación interactiva en Python que permite:

- Ingresar datos de ángulos y distancias manualmente o mediante archivos .csv. 
- Identificar si la poligonal es abierta o cerrada.
- Calcular automáticamente la suma teórica de los ángulos.
- Aplicar correcciones angulares cuando sea necesario.
- Realizar el cálculo de coordenadas a partir del azimut inicial y los datos corregidos.
- Graficar la poligonal con nombres, distancias y coordenadas.
- Exportar los resultados a archivos .csv y la gráfica a formato .png.
  
## Contextualización
Una poligonal es una secuencia de líneas rectas conectadas entre sí mediante ángulos, comúnmente utilizadas en levantamientos topográficos para determinar posiciones sobre el terreno. Estas figuras permiten representar caminos, límites de terrenos, perímetros o recorridos, dependiendo de la aplicación.

Existen dos tipos principales:

- Poligonal cerrada: parte de un punto conocido y regresa a ese mismo punto. Esto permite verificar si hubo errores, ya que se puede comparar la coordenada final calculada con la inicial y aplicar correcciones proporcionales si hay discrepancias.

- Poligonal abierta: no regresa al punto de partida. Aunque es más fácil de ejecutar en campo (como en el caso de una carretera), su análisis es más exigente porque no se puede cerrar el ciclo geométricamente para validar errores de forma directa.

Este contexto es clave para entender por qué los cálculos de ángulos, distancias y coordenadas deben ser tratados cuidadosamente en ambos casos.

## ¿Cómo se abordo el problema?
Para calcular las coordenadas de una poligonal se necesita:

- Las coordenadas de los dos primeros puntos, que establecen la dirección inicial.
- Por cada segmento: la distancia, el ángulo medido, y la dirección (izquierda o derecha).
- El tipo de ángulo usado (interno o externo) y la cantidad total de ángulos.
Con esta información:
- Se calcula el rumbo inicial (dirección del primer segmento).
- Se actualiza el rumbo según los ángulos y las direcciones indicadas.
- A partir del rumbo y la distancia, se determinan las nuevas coordenadas usando funciones trigonométricas.

Si es una poligonal cerrada, se realiza una verificación del cierre geométrico y se aplica una corrección proporcional a las coordenadas para distribuir el error de forma balanceada.

Finalmente, se exportan y grafican los resultados.

# Explicación del código
## 1. Menú
Para facilitar la interacción del usuario con la herramienta, se diseñó un menú principal que se muestra al ejecutar el programa. Este menú permite al usuario elegir entre las diferentes formas de ingreso de datos o salir del programa.
```
ef mostrar_menú(): # Esta función imprime el menú principal para que el usuario pueda interactuar
    print("╔═════════════════════════════════════════════╗")
    print("║        Bienvenido al TopograficTool         ║")
    print("╠═════════════════════════════════════════════╣")
    print("║  1. Ingresar los datos manualmente          ║")
    print("║  2. Cargar los datos desde un archivo(.csv) ║")
    print("║  3. Salir                                   ║")
    print("╚═════════════════════════════════════════════╝")
```
## 2. Opción 1 (Ingresar los datos manualmente)
Cuando el usuario selecciona la opción 1, el programa lo guía paso a paso para ingresar manualmente los datos necesarios para calcular una poligonal, ya sea cerrada o abierta.
El flujo general es el siguiente:
````mermaid
flowchart TD
    A[Inicio - Usuario escoge opción 1] --> B[Seleccionar tipo de poligonal: cerrada o abierta]
    B --> C[Ingresar coordenadas iniciales y azimut]
    C --> D[Ingresar lados y ángulos]
    D --> E[Calcular coordenadas]
    E --> F{Es poligonal cerrada}

    F -- No --> G1[Exportar CSV]
    G1 --> H1[Graficar poligonal]
    H1 --> Z1[Fin]

    F -- Sí --> G[Verificar cierre]
    G --> H{Cierre correcto}

    H -- Sí --> I[Exportar CSV]
    I --> J[Graficar poligonal]
    J --> Z2[Fin]

    H -- No --> K[Aplicar corrección angular]
    K --> L[Corregir distancias y proyecciones]
    L --> M[Aplicar corrección proporcional]
    M --> N[Mostrar coordenadas corregidas]
    N --> O[Exportar CSV]
    O --> P[Graficar poligonal]
    P --> Z3[Fin]
````
### Entrada de datos: 
**1. Solicitar el tipo de poligonal**
```
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
```
**2. Ingreso de datos:**
Esta función guía al usuario en el ingreso de los datos topográficos base para iniciar el cálculo de la poligonal. El procedimiento contempla el ingreso de:
- Coordenadas del punto inicial (X, Y): en metros, pueden ser valores reales (UTM, por ejemplo) o de un sistema local arbitrario.
- Azimut inicial: solicitado en sistema sexagesimal (grados, minutos y segundos), el cual es validado para evitar errores comunes. Luego, se convierte a grados decimales, formato requerido para realizar los cálculos posteriores como la proyección de distancias.

Esta etapa es crucial, ya que define el punto de partida y la dirección inicial del levantamiento topográfico.

**Retorna:**
- x_inicial (float): Coordenada Este (X) del punto de partida.
- y_inicial (float): Coordenada Norte (Y) del punto de partida.
- azimut_decimal (float): Dirección inicial expresada en grados decimales.
```
def ingreso_datos():
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
```
**3. Entrada de datos (lados y ángulos)**
Esta función solicita al usuario los datos topográficos de cada lado de la poligonal: la distancia, la dirección de giro (izquierda o derecha) y el ángulo en sistema sexagesimal.
Si se trata de una poligonal cerrada, se consulta además si los ángulos son internos o externos para aplicar una corrección angular automática que garantice el cierre geométrico.
Se asegura que todos los giros tengan la misma dirección para coherencia geométrica.
Cada ángulo ingresado se convierte a decimal y se acumula para aplicar, en el caso cerrado, la corrección proporcional por error angular.

**Retorna:**
- Una lista de tuplas con: (distancia, ángulo_decimal, dirección)
- Tipo de ángulo ('i' o 'e') si es poligonal cerrada, o None si es abierta.
```
def ingresar_lados_y_angulos(poligonal_cerrada=False):

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
```
**4. Calcular coordenadas y proyecciónes:**
Calcula las coordenadas de los puntos de una poligonal a partir de un punto inicial, un azimut inicial, y los lados con sus respectivos ángulos y direcciones de giro.

```

def calcular_coordenadas(x_inicial, y_inicial, azimut_inicial, lados, tipo_angulo):
       
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
```

***Cálculo de azimut***
- Para giro hacia la izquierda
````math
$$
\text{Azimut\_nuevo} = \text{Azimut\_anterior} + \text{Ángulo\_corregido}
$$
````
- Para giro hacia la derecha
````math
$$
\text{Azimut\_nuevo} = \text{Azimut\_anterior} + \text{Ángulo\_corregido}
$$
````
***Mantener el azimut en el rango convencional (o°-360°)***
````math
$$
\text{Azimut} = \text{Azimut} / 360^\circ
$$
````
***Convertir azimut a radianes***
````math
$$
\text{Radianes} = \frac{\text{Grados} \cdot \pi}{180}
$$
````
```
# Conversión del ángulo de sexagesimal a decimal
    azimut_decimal = grados + minutos / 60 + segundos / 3600
    
    # Muestra el azimut convertido para verificación
    print(f"El azimut inicial en decimal: {azimut_decimal:.3f}°")
    
    # Devuelve los valores necesarios
    return x_inicial, y_inicial, azimut_decimal
```
### Calculo de coordenadas sin correción
***Coordenadas Norte***
````math
$$
Y = Y_{\text{anterior}} + \Delta N
$$
````
***Coordenadas Este***
````math
$$
X = X_{\text{anterior}} + \Delta E
$$
````
### En poligonal abierta
No se necesitan cálculos de corrección, simplemente exporta los datos a un .csv y hace la gráfica
### En poligonales cerradas
1. Verifica el cierre de la poligonal:
```
def verificar_cierre(coordenadas, tolerancia=0.01):

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
```
Si está cerrada, procede a guardar las coordenadas dadas en un .csv y gráficar, si no está cerrada, continua con los cálculos.
 1.1 Corregir coordenadas:
 
***Suma teórica de angulos***
```math
$$
\text{Ángulos\_internos} = (n - 2) \times 180^\circ
$$
````
````math
$$
\text{Ángulos\_externos} = (n + 2) \times 180^\circ
$$
````
```
def calcular_suma_teorica_angulos(n: int, tipo_angulo: str) -> float:
    # Si los ángulos son internos, la fórmula es (n - 2) * 180°
    if tipo_angulo == 'i':
        return (n - 2) * 180
    else:
        # Si los ángulos son externos, la fórmula es (n + 2) * 180°
        return (n + 2) * 180
```






***error_angular***
```math
$$
\text{Corrección\_angular\_total} = \text{Suma\_teórica} - \sum \text{ángulos\_observados}
$$
````
***corrección por ángulo***
````math
$$
\text{Corrección\_por\_ángulo} = \frac{\text{Error\_angular}}{n}
$$
````
```
def calcular_correccion_angulos(n, tipo_angulo, suma_angular_observada):

    # Calcula la suma teórica según el número de lados y tipo de ángulo
    suma_teorica = calcular_suma_teorica_angulos(n, tipo_angulo)

    # Calcula el error angular como la diferencia entre la suma teórica y la observada
    error = suma_teorica - suma_angular_observada

    # La corrección que se aplicará a cada ángulo es el error dividido entre la cantidad de ángulos
    correccion = error / n

    return correccion, error, suma_teorica
```
***ángulo corregido***
````math
$$
\text{Ángulo\_corregido} = \text{Ángulo\_observado} + \text{Corrección\_por\_ángulo}
$$
````

### Cálculo de proyecciones en x y y, y correciones.
***Proyecciones en Nortes***
````math
$$
\Delta N = \cos(\text{azimut}) \cdot \text{distancia}
$$
````
***Proyecciones en Estes***
````math
$$
\Delta E = \sin(\text{azimut}) \cdot \text{distancia}
$$
````


Utilizadas en ese orden, con la siguiente lógica 
````mermaid
flowchart TD
    A[Inicio] --> B[Ingresar datos]
    B --> B1[Cantidad de lados: n]
    B <--> B2[Ángulos observados]
    B --> B3[Distancias]
    B --> B4[Coordenadas iniciales X y Y]

    B1 --> C{Tipo de ángulo}
    C -->|Internos| D1["Suma teórica = (n - 2) * 180"]
    C -->|Externos| D2["Suma teórica = (n + 2) * 180"]

    D1 --> E[Sumar ángulos observados]
    D2 --> E

    E --> F["Error angular = Suma teórica - Suma observada"]
    F --> G["Corrección por ángulo = Error / n"]
    G --> H["Ángulo corregido = Observado + Corrección"]

    H --> I{¿Girar a la izquierda o derecha?}
    I -->|Izquierda| J1["Azimut nuevo = Azimut anterior + Ángulo corregido"]
    I -->|Derecha| J2["Azimut nuevo = Azimut anterior - Ángulo corregido"]

    J1 --> K
    J2 --> K

    K["Azimut = Azimut mod 360"] --> L["Azimut radianes = (Grados * π) / 180"]

    L --> M1["Delta Norte = cos(azimut) * distancia"]
    L --> M2["Delta Este = sen(azimut) * distancia"]

    M1 --> N1["X nueva = X anterior + Delta Norte"]
    M2 --> N2["Y nueva = Y anterior + Delta Este"]

    N1 --> O1[Guardar coordenada X]
    N2 --> O2[Guardar coordenada Y]

    O1 --> P{¿Hay más puntos?}
    O2 --> P

    P -->|Sí| B2
    P -->|No| FIN
````
```
def calcular_coordenadas(x_inicial, y_inicial, azimut_inicial, lados, tipo_angulo):  
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
```
### Correciones en proyecciones y coordenadas finales.
***Error de cierre***
````math
$$
\text{Error}_x = X_{\text{inicial}} - X_{\text{final}}
$$
````
```
def verificar_cierre(coordenadas, tolerancia=0.01):
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
```
````math
$$
\text{Error}_y = Y_{\text{inicial}} - Y_{\text{final}}
$$
````
***Total distancia***
```math
\text{distancia\_total}_i = \left( \sum_{} distancias \right)
```
***Distancias acumuladas***
````math
$$
\text{distancia\_acumulada}_i = \sum_{k=1}^{i} d_k
$$

```` 
***Coordenadas corregidas***
````math
$$
x_{\text{corregido}} = x_i + \left( \frac{d_i}{D} \right) \cdot e_x
$$
````
````math
$$
y_{\text{corregido}} = y_i + \left( \frac{d_i}{D} \right) \cdot e_y
$$
````
Usando la siguiente lógica
````mermaid
flowchart TD
    A{¿Hay más puntos?}
    A -- No --> B1[Calcular diferencia entre X inicial y X final]
    A -- No --> B2[Calcular diferencia entre Y inicial y Y final]
    B1 --> C[Asignar error en X como ex]
    B2 --> D[Asignar error en Y como ey]
    C --> E[Sumar todas las distancias para obtener D]
    D --> E
    E --> F[Para cada punto: calcular distancia acumulada hasta i]
    F --> G[Corregir X sumando proporcion de ex segun distancia acumulada]
    F --> H[Corregir Y sumando proporcion de ey segun distancia acumulada]
    G --> I[Guardar X corregido]
    H --> J[Guardar Y corregido]
    I --> K{¿Quedan coordenadas por corregir?}
    J --> K
    K -- Si --> F
    K -- No --> L[Fin del proceso]
````
```
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
```



## Para graficar
````
def graficar_poligonal(coordenadas, nombre_archivo="poligonal.png"):
    # Crea una nueva figura de tamaño 10x8 pulgadas para la visualización
    plt.figure(figsize=(10, 8))

    # Separa las coordenadas X y Y en dos listas diferentes
    xs = [x for x, y in coordenadas]
    ys = [y for x, y in coordenadas]

    # Dibuja la poligonal conectando los puntos con líneas y marcando cada vértice con un círculo
    plt.plot(xs, ys, marker='o', linestyle='-', color='blue')

    # Recorre todos los puntos para etiquetarlos y mostrar la distancia entre cada par de puntos consecutivos
    for i, (x, y) in enumerate(coordenadas):
        # Agrega una etiqueta "P1", "P2", etc., ligeramente desplazada hacia arriba
        plt.text(x, y + 0.5, f"P{i+1}", fontsize=9, ha='center', va='bottom', color='darkred')
        
        # Si no es el primer punto, calcular y mostrar la distancia al punto anterior
        if i > 0:
            x0, y0 = coordenadas[i - 1]  # Punto anterior
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

````
## Explicación general
### 1. Módulo principal (`main.py`)
Contiene el menú interactivo y la lógica general del programa.

### 2. Cálculos y utilidades (`utils.py`)
- `calcular_suma_teorica_angulos()`
- `calcular_correccion_angulos()`
- `calcular_coordenadas()`
- etc.

### 3. Entrada/salida (`io.py`)
- `leer_csv()`
- `exportar_a_csv()`
- `graficar_poligonal()`

### 4. Interfaz amigable
Mensajes motivadores, validación de entradas, estilo relajado y amigable.


## Diagrama de flujo del programa

````mermaid
flowchart TD
    A[Inicio] --> B[Solicitar tipo de poligonal]
    B --> C{¿Es poligonal cerrada?}
    C -->|Sí| D[Solicitar tipo de angulo: interno o externo]
    C -->|No| E[Continuar sin angulos]
    D --> F[Solicitar numero de lados y angulos]
    E --> F
    F --> G[Solicitar coordenadas iniciales y azimut]
    G --> H{¿Entrada manual o por CSV?}
    H -->|Manual| I[Ingresar lados y angulos manualmente]
    H -->|CSV| J[Leer datos desde archivo CSV]
    I --> K[Convertir angulos a decimales]
    J --> K
    K --> L{¿Es poligonal cerrada?}
    L -->|Sí| M[Corregir suma de angulos observados]
    L -->|No| N[Calcular coordenadas sin correccion angular]
    M --> O[Aplicar correccion angular proporcional]
    O --> P[Calcular coordenadas]
    N --> P
    P --> Q[Aplicar correccion de cierre si es cerrada]
    Q --> R[Exportar resultados a CSV]
    R --> S[Graficar poligonal y guardar PNG]
    S --> T[Fin]
````
