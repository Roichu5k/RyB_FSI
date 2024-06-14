### Memoria del Trabajo: Modificación de Código Python para Algoritmos de Búsqueda en Grafos

#### Introducción

En este trabajo, hemos recibido un código base en Python que implementa un algoritmo de búsqueda en grafos. Nuestra tarea ha sido modificarlo para permitir la búsqueda de rutas entre dos nodos en un grafo utilizando cuatro algoritmos distintos: búsqueda en amplitud (BFS), búsqueda en profundidad (DFS), búsqueda por ramificación y acotación, y búsqueda por ramificación y acotación con subestimación. 

El objetivo es obtener, para cada algoritmo, los nodos generados, los nodos visitados y las rutas encontradas desde un nodo de inicio (A) hasta un nodo de destino (B). A continuación, se describe el proceso de modificación del código y los resultados obtenidos con cada algoritmo.

#### Algoritmos Implementados

1. **Búsqueda en Amplitud (Breadth-First Search, BFS)**
   
   Este algoritmo explora el grafo nivel por nivel, comenzando desde el nodo de inicio y explorando todos sus vecinos antes de pasar al siguiente nivel de nodos. Es ideal para encontrar la ruta más corta en términos de número de aristas.

2. **Búsqueda en Profundidad (Depth-First Search, DFS)**

   La búsqueda en profundidad explora cada rama del grafo tan lejos como sea posible antes de retroceder. Este enfoque es útil para explorar todas las posibles rutas, pero no garantiza la ruta más corta.

3. **Búsqueda por Ramificación y Acotación (Branch and Bound)**

   Este algoritmo explora los caminos basándose en una función de coste, expandiendo el nodo que tiene el menor coste acumulado hasta el momento. Esto ayuda a reducir el número de nodos a explorar al enfocarse en las rutas más prometedoras.

4. **Búsqueda por Ramificación y Acotación con Subestimación (Branch and Bound with Underestimation)**

   Similar al algoritmo anterior, pero incorpora una heurística que subestima el coste restante para llegar al destino. Esto permite una exploración más eficiente y rápida hacia la solución óptima.

#### Modificación del Código

El código base implementaba solo un algoritmo de búsqueda simple. A continuación, describimos los cambios realizados para implementar cada uno de los cuatro algoritmos mencionados:

1. **Incorporación de Estructuras de Datos Apropiadas:**
   - Para BFS y DFS, utilizamos una cola y una pila, respectivamente, para gestionar los nodos por explorar.
   - Para Ramificación y Acotación, usamos una cola de prioridad que ordena los nodos según el coste acumulado.
   - Para Ramificación y Acotación con Subestimación, añadimos una función heurística que subestima el coste restante y ajustamos la cola de prioridad en consecuencia.

2. **Registro de Nodos Generados y Visitados:**
   - Implementamos contadores y listas para registrar los nodos generados y visitados durante la búsqueda, permitiendo así evaluar la eficiencia de cada algoritmo.

3. **Trazado de la Ruta:**
   - Modificamos el algoritmo para registrar la ruta completa desde el nodo de inicio hasta el nodo de destino en cada búsqueda.

4. **Función Heurística:**
   - Para el algoritmo con subestimación, desarrollamos una función heurística simple que estima el coste restante basándose en la distancia euclidiana en un grafo 

#### Conclusiones

La implementación y comparación de estos cuatro algoritmos nos permitió observar sus diferentes enfoques y eficiencias en la búsqueda de rutas en un grafo. La búsqueda en amplitud y la búsqueda en profundidad son básicas pero útiles para explorar rutas de manera exhaustiva. La ramificación y acotación, especialmente cuando se utiliza con subestimación, ofrece una exploración más eficiente y rápida hacia la solución óptima, aprovechando la priorización basada en el coste y las heurísticas.

Este ejercicio ha demostrado la importancia de seleccionar el algoritmo adecuado según los requisitos específicos de la búsqueda y las características del grafo.
