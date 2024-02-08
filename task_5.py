from binary_tree import Node, draw_tree


def dfs(node, visited=None):
    if visited is None:
        visited = set()
    if node:
        visited.add(node)

        alpha = int((1 - len(visited) * 0.1) * 255)
        node.color = "#%02x%02x%02x%02x" % (0, 0, 255, alpha)

        dfs(node.left, visited)
        dfs(node.right, visited)
    return visited


def bfs(start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node and node not in visited:
            visited.add(node)
            alpha = int((1 - len(visited) * 0.1) * 255)
            node.color = "#%02x%02x%02x%02x" % (0, 0, 255, alpha)

            queue.append(node.left)
            queue.append(node.right)
    return visited


def show_menu():
    print("Select option:")
    print("1. DFS algorithm")
    print("2. BFS algorithm")
    print("3. Exit")


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    is_active = True
    while is_active:
        show_menu()
        try:
            option = int(input())
            if 1 > option > 3:
                raise ValueError("Incorect option")
            if option == 3:
                print("\nHave a nice day")
            elif option == 1:
                visited_dfs = dfs(root)
                draw_tree(root)
            elif option == 2:
                visited_bfs = bfs(root)
                draw_tree(root)

            is_active = False
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
        except KeyboardInterrupt:
            print("\nHave a nice day")
            is_active = False
