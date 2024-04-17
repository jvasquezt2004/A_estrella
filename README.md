# Explicacion del algoritmo

## Clase Puzzle

Representa diferentes estados del puzzle, guarda la posicion del tablero, el costo que se lleva hasta ahora, la heuristica ya definida con la funcion que se basa en la distancia manhattan

### Metodo calculate_distance

la clave es el uso de np.where que proporciona la ubicacion exacta del numero que se esta buscando al momento, lo retorna como una tupla, de ahi que se tengan que seleccionar las posiciones en un arreglo

### Metodo generate_sucesores

Se obtiene la posicion del y en base a las direcciones basadas en arriba, abajo, derecha e izquierda los recorre y ve si es posible el movimient para ponerlo como hijo del nodo padre

## Clase Solver

Maneja como tal la logica del algoritmo A\* con una cola de prioridad

### Metodo solve

Coloca en la cola los datos y va revisando mientras recorre la cola si es el resultado final con el mejor costo

finalmente para imprimir se invierte la cola para mostrar el orden de forma correcta
