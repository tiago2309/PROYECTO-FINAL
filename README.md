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
````

**********Aqui va diagrama del funcionamiento por encima, sin calculos**********
````
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
```
Internos: (n − 2) × 180°

Externos (n + 2) × 180°
```
***error_angular***
```
suma teorica - sumatoria observada
````
***corrección por ángulo***
````
error_angular / n(número le lados)
````
***ángulo corregido***
````
ángulo + corrección por ángulo
````
***Cálculo de azimut***
- Para giro hacia la izquierda
````
azimut nuevo = azimut anterior + ángulo corregido
````
- Para giro hacia la derecha
````
azimut nuevo = azimut anterior + ángulo corregido
````
***Mantener el azimut en el rango convencional (o°-360°)***
````
azimut = azimut % 360
````
***Convertir azimut a radianes***
````
Radianes = (Grados * π) / 180
````
Utilizadas en ese orden, con la siguiente lógica 
````
*************diagrama de la correcion de angulos********
````
### Cálculo de proyecciones en x y y, y correciones.
***Proyecciones en Nortes***
````
DeltaN= Cos(az) * distancia 
````
***Proyecciones en Estes***
````
DeltaE= Sen(az) * distancia 
````
````
----------------diagrama----------
````
### Calculo de coordenadas sin correción
***Coordenadas Norte***
````
x =`x anterior + DeltaN
````
***Coordenadas Este***
````
x = x anterior +DeltaE
````
### Correciones en proyecciones y coordenadas finales.
***Error de cierre***
````
Error en x = Coordenada en x inicial - coordenada en x final
Error en y = Coordenada en y inicial - coordenada en y final
````
***Proyecciones en Nortes***
````
Delta= Cos(az) * distancia 
````


