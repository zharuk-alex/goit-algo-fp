import networkx as nx
import matplotlib.pyplot as plt
from binary_tree import Node


def visualize_heap(node, pos, graph=None, x=0, y=0, layer=1):
    if graph is None:
        graph = nx.DiGraph()
        pos[node.id] = (x, y)

    graph.add_node(node.id, color=node.color, label=node.val)

    if node.left:
        graph.add_edge(node.id, node.left.id)
        next_x, next_y = x - 1 / 2**layer, y - 1
        pos[node.left.id] = (next_x, next_y)
        visualize_heap(node.left, pos, graph, next_x, next_y, layer + 1)

    if node.right:
        graph.add_edge(node.id, node.right.id)
        next_x, next_y = x + 1 / 2**layer, y - 1
        pos[node.right.id] = (next_x, next_y)
        visualize_heap(node.right, pos, graph, next_x, next_y, layer + 1)

    return graph


def draw_heap(root):
    pos = {}
    heap_graph = visualize_heap(root, pos)
    colors = [node[1]["color"] for node in heap_graph.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in heap_graph.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        heap_graph,
        pos=pos,
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    # Відображення купи
    draw_heap(root)
