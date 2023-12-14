# Search methods

import search, time

ab = search.GPSProblem('A','B'
                       , search.romania)

print("\n\t\t\t- A -> B -")
print("\n\t\t-Amplitud-")

inicio = time.time()
ruta_amplitud = search.breadth_first_graph_search(ab).path()
tiempo_amplitud = time.time() - inicio

print("Ruta: " + str(ruta_amplitud))
print("Tiempo en Amplitud: " + str(tiempo_amplitud) + " segundos")

print("\n\t\t-Profundidad-")
inicio = time.time()
print("Ruta: " + str(search.depth_first_graph_search(ab).path()))
print("Tiempo en Profundidad: " + str(time.time() - inicio))

print("\n\t\t-Ramificación y Acotación-")
inicio = time.time_ns()
print("Ruta: " + str(search.RyA(ab).path()))
print("Tiempo en Ramificación y Acotación: " + str(time.time_ns() - inicio))


print("\n\t\t-Ramificación y Acotiación con subestimación-")
inicio = time.time_ns()
print("Ruta: " + str(search.RyAsub(ab).path()))
print("Tiempo de Ramificación y Acotiación con subestimación: " + str(time.time_ns() - inicio))


print()
print()

oe = search.GPSProblem('O', 'E', search.romania)
print("\n\t\t\t- O -> E -")
print("\n\t\t-Amplitud-")
inicio = time.time_ns()
print("Ruta: " + str(search.breadth_first_graph_search(oe).path()))
print("Tiempo en Amplitud: " + str(time.time_ns() - inicio))

print("\n\t\t-Profundidad-")
inicio = time.time_ns()
print("Ruta: " + str(search.depth_first_graph_search(oe).path()))
print("Tiempo en Profundidad: " + str(time.time_ns() - inicio))

print("\n\t\t-Ramificación y Acotación-")
inicio = time.time_ns()
print("Ruta: " + str(search.RyA(oe).path()))
print("Tiempo en Ramificación y Acotación: " + str(time.time_ns() - inicio))

print("\n\t\t-Ramificación y Acotiación con subestimación-")
inicio = time.time_ns()
print("Ruta: " + str(search.RyAsub(oe).path()))
print("Tiempo en Ramificación y Acotiación con subestimación: " + str(time.time_ns() - inicio))


print()
print()

oe = search.GPSProblem('G', 'Z', search.romania)
print("\n\t\t\t- G -> Z -")
print("\n\t\t-Amplitud-")
inicio = time.time_ns()
print("Ruta: " + str(search.breadth_first_graph_search(oe).path()))
print("Tiempo en Amplitud: " + str(time.time_ns() - inicio))

print("\n\t\t-Profundidad-")
inicio = time.time_ns()
print("Ruta: " + str(search.depth_first_graph_search(oe).path()))
print("Tiempo en Profundidad: " + str(time.time_ns() - inicio))

print("\n\t\t-Ramificación y Acotación-")
inicio = time.time_ns()
print("Ruta: " + str(search.RyA(oe).path()))
print("Tiempo en Ramificación y Acotación: " + str(time.time_ns() - inicio))

print("\n\t\t-Ramificación y Acotiación con subestimación-")
inicio = time.time_ns()
print("Ruta: " + str(search.RyAsub(oe).path()))
print("Tiempo en Ramificación y Acotiación con subestimación: " + str(time.time_ns() - inicio))
