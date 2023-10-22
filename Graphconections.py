import networkx as nx
import matplotlib.pyplot as plt

# Grafo con las conexiones y pesos/distancias entre las ciudades
graph = nx.Graph()

graph.add_edge('Sevilla', 'Madrid', weight=531)
graph.add_edge('Sevilla', 'Malaga', weight=207)
graph.add_edge('Madrid', 'Bilbao', weight=395)
graph.add_edge('Madrid', 'Barcelona', weight=622)
graph.add_edge('Madrid', 'Alicante', weight=437)
graph.add_edge('Madrid', 'Oviedo', weight=445)
graph.add_edge('Bilbao', 'Barcelona', weight=606)
graph.add_edge('Barcelona', 'Alicante', weight=538)
graph.add_edge('Malaga', 'Melilla', weight=221)
graph.add_edge('Malaga', 'Barcelona', weight=1006)
graph.add_edge('Malaga', 'Madrid', weight=534)
graph.add_edge('Melilla', 'Malaga', weight=221)

start_city = 'Sevilla' #ciudad de inicio en el grafo
end_city = 'Barcelona' #Ciudad a la que se quiere llegar

# Obtener todas las rutas posibles con un máximo de 3 ciudades intermedias
routes = nx.all_simple_paths(graph, start_city, end_city, cutoff=4)

distances = []

for route in routes:
    distance = sum(graph[route[i]][route[i+1]]['weight'] for i in range(len(route) - 1))
    distances.append((route, distance))

distances.sort(key=lambda x: x[1])

# Crear una lista con los caminos más cortos
shortest_paths = [distances[i][0] for i in range(min(3, len(distances)))]

# Generar los gráficos de los caminos más cortos
for i, path in enumerate(shortest_paths):
    # Crear un nuevo grafo solo con las conexiones del camino actual
    path_graph = nx.Graph()
    path_graph.add_edges_from(list(zip(path[:-1], path[1:])))

    # Obtener las posiciones de los nodos en el grafo
    pos = nx.spring_layout(path_graph, seed=42)

    # Dibujar los nodos y las conexiones del camino actual
    nx.draw_networkx(path_graph, pos, with_labels=True, node_color='lightblue',
                     node_size=500, font_size=10, font_color='black',
                     edge_color='gray', width=2)

    # Obtener las distancias de cada conexión en el camino actual
    path_distances = [graph[path[j]][path[j + 1]]['weight'] for j in range(len(path) - 1)]

    # Crear una etiqueta con las distancias y agregarlas a los nodos
    edge_labels = {tuple(path[j: j + 2]): str(path_distances[j]) + " km" for j in range(len(path) - 1)}
    nx.draw_networkx_edge_labels(path_graph, pos, edge_labels=edge_labels)



    plt.title(f"Camino más corto {i+1} - Distancia final: {distances[i][1]} km")
    plt.axis('off')
    plt.show()
