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
### Correciones en proyecciones y coordenadas finales.
***Error de cierre***
````math
$$
\text{Error}_x = X_{\text{inicial}} - X_{\text{final}}
$$
````
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
### Para poligonal abierta básicamente hace lo mismo pero sin la corrección de ángulos
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
    A[Inicio] --> B[Mostrar menú]
    B --> C{Opción seleccionada}
    
    C -->|1: Ingreso manual| D1[Solicitar tipo de poligonal]
    D1 --> E1[Ingresar coordenadas iniciales y azimut]
    E1 --> F1[Ingresar lados y ángulos]
    F1 --> G1{¿Poligonal cerrada?}
    
    G1 -->|Sí| H1[Corregir ángulos]
    H1 --> I1[Calcular coordenadas]
    G1 -->|No| I1
    
    I1 --> J1[Graficar poligonal]
    J1 --> K1[Exportar coordenadas a CSV]
    K1 --> L1[Volver al menú]

    C -->|2: Ingreso por CSV| D2[Leer datos desde archivo CSV]
    D2 --> E2[Solicitar tipo de poligonal]
    E2 --> F2[Ingresar coordenadas iniciales y azimut]
    F2 --> G2{¿Poligonal cerrada?}
    
    G2 -->|Sí| H2[Corregir ángulos]
    H2 --> I2[Calcular coordenadas]
    G2 -->|No| I2

    I2 --> J2[Graficar poligonal]
    J2 --> K2[Exportar coordenadas a CSV]
    K2 --> L2[Volver al menú]

    C -->|3: Salir| Z[Fin del programa]
````
