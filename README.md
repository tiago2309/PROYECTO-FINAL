# PROYECTO-FINAL
## TopograficTool-Herramienta para cálculos topograficos en Ingenieria Civil
## Autores
- Maria Camila Palomo Avila
- Santiago Ramos Barriga
  
Curso: Programación de Computadores    
Grupo: 404 CNF (Chill Not Found)    
Universidad Nacional de Colombia  

## Contexto
En la Ingeniería Civil, una de las actividades fundamentales en proyectos de obras civiles (como carreteras, redes de acueducto, edificaciones, puentes, etc.) es la topografía, que permite conocer y representar el terreno de forma precisa, lo que es necesario para la planificación, desarrollo, diseño y ejecución de obras civiles.  Actualmente estamos cursando la asignatura de Geomática Básica dónde hemos encontrdo dificultades a la hora de hallar soluciones rapidas a los problemas dados, ya que la toma de datos se realiza muchas veces manualmente, en clases prácticas que se dan bajo diferentes condiciones, muchas veces no ideal, con tiempo limitado lo que no siempre permite repasar a fondo los procedimientos ni validar datos con precisión, tomando los datos manuelmente o en hojas de cálculo, haciendo cálculos repetitivos, y con más probabilidad a error, lo cual consume tiempo (que podría usarse en interpretación, análisis o mejora del diseño) y puede generar errores, que al momento de aplicar en la vida profesional y un proyecto real, trae consecuencias costosas. Se necesita una herramienta por consola que automatice este proceso para estudiantes y técnicos.

### Solución 
La idea de este programa es crear una herramienta por consola en Python llamada TopograficTool, que permita a los usuarios calcular coordenadas, cierres, y correcciones de poligonales (abiertas y cerradas) usando datos ingresados manualmente o desde archivos ".csv"(los más usados en topografia).Con herramientas automatizadas es más fácil llevar un registro digital de cada ejercicio, estudiante o grupo de trabajo, por lo que creamos una herramienta ligera por consola que puede ser el puente entre lo que se enseña en clase y lo que se aplica en campo, entendiendo también que la transformación digital en ingeniería exige que los nuevos profesionales sean capaces de crear sus propias soluciones. Como estudiantes de la carrera y la materia, decidimos que no queremos que el programa sea algo totalmente serio y académico, comprendiendo el estrés que produce la vida académica, queremos aliviarlo con una consola que sea interactiva, donde no solo el usuario decide que hacer, si no que ve una interfaz diferente, y con mensajes motivadores, que lo hagan salir de la rutina.

## ¿Cómo funciona?
Un estudiante está en clase de Geomática. Luego de levantar datos con el teodolito (insumo utilizado en las prácticas para medir distancias y ángulos de un terreno), debe procesarlos:  

- Presentar un menú al usuario, para que elija los cálculos a trabajar.
- Pedir que ingrese datos iniciales.
- Permitirle elegir al usuario con que tipo de poligonal y ángulos trabajará
- Cargar los puntos medidos (distancias, coordenadas)
- Verificar si es poligonal abierta o cerrada
- Calcular las coordenadas de los puntos y las distancias
- Corregir errores
- Exportar los resultados en la consola, o en archivo .csv

## ¡Antes de!

Debemos entender primero como funcionan los calculos a continuación, que se nesecita para calcular una poligonal cerrada o abierta:  

Una poligonal es una sucesión de lineas que se conectan entre si y con las cuales se miden distancias y angulos, para calcular coordenadas y utilizarlas para representar un terreno (y con esto hacer muchas cosas más, pero no es el punto ahora).  

Una poligonal abierta se presenta cuando el punto final no coincide con el inicial (como las carreteras).  
En una poligonal cerrada el punta final coincide con el inicial (como lotes, terrenos).  

Teniendo en cuenta que el objetivo es calcular las coordenadas finales de una poligonal, para los dos casos se debe ingresar:
- Coordenas y ángulos de los dos puntos iniciales (Norte y Este)
- Distancias, ángulos, cantidad de ángulos, tipos de ángulos (internos o externos), por cada punto de la poligonal.  
  
Con éstos datos se debe:

### En poligonales cerradas
Corregir los ángulos internos y externos, para que la suma sea coherente y con ésto calcular el azimut. Para hacer esto se nesecitan las siguientes formulas: 
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

### Para poligonal abierta básicamente hace lo mismo pero sin la corrección de ángulos

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
