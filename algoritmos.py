from collections import deque

def bfs_con_camino(grafo, inicio):
    visitado = set()
    cola = deque([(inicio, None, 0)])  # (nodo, predecesor, distancia)
    iteracion = 1

    print(f"{'Iteración':<10} {'Longitud de camino':<20} {'Actual':<10} {'Predecesor'}")
    while cola:
        nodo, predecesor, distancia = cola.popleft()
        if nodo not in visitado:
            print(f"{iteracion:<10} {distancia:<20} {str(nodo):<10} {str(predecesor)}")
            iteracion += 1
            visitado.add(nodo)
            vecinos = sorted(grafo[nodo])
            for vecino in vecinos:
                if vecino not in visitado:
                    cola.append((vecino, nodo, distancia + 1))

def dfs_con_camino(grafo, inicio):
    visitados = set()
    pila = [(inicio, None)]
    en_pila = {inicio}  # 👈 conjunto para evitar duplicados en la pila
    predecesores = {}
    profundidad = {inicio: 0}
    iteracion = 1

    print(f"{'Iteración':<10} {'Long. camino':<17} {'Actual':<10} {'Predecesor':<12} {'Pila actualizada'}")
    print("-" * 90)

    while pila:
        actual, padre = pila.pop()
        en_pila.discard(actual)

        if actual not in visitados:
            visitados.add(actual)
            predecesores[actual] = padre
            prof = profundidad[actual]

            # Apilar vecinos únicos
            for vecino in sorted(grafo[actual]):
                if vecino not in visitados and vecino not in en_pila:
                    pila.append((vecino, actual))
                    en_pila.add(vecino)
                    if vecino not in profundidad:
                        profundidad[vecino] = prof + 1

            pila_estado = [nodo for nodo, _ in pila]
            print(f"{iteracion:<10} {prof:<17} {actual:<10} {padre or 'None':<12} {pila_estado}")
            iteracion += 1

    print(f"\nPila final: {pila}")

def dfs_con_camino(grafo, inicio):
    visitados = set()
    pila = [(inicio, None)]
    en_pila = {inicio}  # 👈 conjunto para evitar duplicados en la pila
    predecesores = {}
    profundidad = {inicio: 0}
    iteracion = 1

    print(f"{'Iteración':<10} {'Long. camino':<17} {'Actual':<10} {'Predecesor':<12} {'Pila actualizada'}")
    print("-" * 90)

    while pila:
        actual, padre = pila.pop()
        en_pila.discard(actual)

        if actual not in visitados:
            visitados.add(actual)
            predecesores[actual] = padre
            prof = profundidad[actual]

            # Apilar vecinos únicos
            for vecino in sorted(grafo[actual]):
                if vecino not in visitados and vecino not in en_pila:
                    pila.append((vecino, actual))
                    en_pila.add(vecino)
                    if vecino not in profundidad:
                        profundidad[vecino] = prof + 1

            pila_estado = [nodo for nodo, _ in pila]
            print(f"{iteracion:<10} {prof:<17} {actual:<10} {padre or 'None':<12} {pila_estado}")
            iteracion += 1

    print(f"\nPila final: {pila}")

import pandas as pd

def dfs(grafo, inicio):
    visitados = set()
    pila = [(inicio, None)]
    en_pila = {inicio}
    predecesores = {}
    profundidad = {inicio: 0}
    iteracion = 1
    tabla_datos = []  # 👈 Aquí guardamos los datos por fila

    while pila:
        actual, padre = pila.pop()
        en_pila.discard(actual)

        if actual not in visitados:
            visitados.add(actual)
            predecesores[actual] = padre
            prof = profundidad[actual]

            # Apilar vecinos únicos (en orden ascendente)
            for vecino in sorted(grafo[actual]):
                if vecino not in visitados and vecino not in en_pila:
                    pila.append((vecino, actual))
                    en_pila.add(vecino)
                    profundidad[vecino] = prof + 1

            # Guardar datos de esta iteración
            pila_estado = [nodo for nodo, _ in pila]
            tabla_datos.append({
                'Iteración': iteracion,
                'Long. camino': prof,
                'Actual': actual,
                'Predecesor': padre or 'None',
                'Pila actualizada': str(pila_estado)  # Convertimos a string para mejor visualización
            })
            iteracion += 1

    # Creamos el DataFrame y lo mostramos
    df = pd.DataFrame(tabla_datos)
    print("Recorrido final:", list(predecesores.keys()))
