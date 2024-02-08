import heapq
import networkx as nx
import matplotlib.pyplot as plt


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]

    paths = {vertex: [] for vertex in graph}
    paths[start] = [start]

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_vertex] + [neighbor]
                heapq.heappush(pq, (distance, neighbor))

    return paths


if __name__ == "__main__":
    cities_graph = {
        "NY": {"LA": 5, "CH": 10},
        "LA": {"NY": 5, "DA": 3},
        "CH": {"NY": 10, "DA": 2},
        "DA": {"LA": 3, "CH": 2, "HO": 4},
        "HO": {"DA": 4},
        "SF": {"HO": 5, "DA": 4, "LA": 3},
    }

    start_vertex = "DA"
    target_vertex = "NY"
    paths = dijkstra(cities_graph, start_vertex)
    path_highlight = paths[target_vertex]

    G = nx.DiGraph()

    for node, edges in cities_graph.items():
        for adjacent, weight in edges.items():
            G.add_edge(node, adjacent, weight=weight)

    pos = nx.circular_layout(G)

    nx.draw(
        G, pos, with_labels=True, node_size=400, node_color="lightblue", font_size=10
    )

    nx.draw_networkx_edge_labels(
        G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
    )

    edges_in_path = [
        (path_highlight[i], path_highlight[i + 1])
        for i in range(len(path_highlight) - 1)
    ]

    nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color="red", width=2)

    plt.title(f"The shortest paths from {start_vertex} to {target_vertex}")
    plt.get_current_fig_manager().set_window_title(
        f"The shortest paths from {start_vertex} to {target_vertex}"
    )
    plt.show()

    G = nx.DiGraph()

    print(f"The shortest paths from {start_vertex} to all other nodes are:")
    for destination, path in paths.items():
        print(f" - {destination}: {path}")
