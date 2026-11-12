
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def binary_tree_bfs(root):
    if not root:
        return

    queue = deque([root])
    path = []

    while queue:
        current = queue.popleft()
        path.append(current.data)

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)

    print("Binary Tree BFS Traversal: " + " - ".join(path))


def binary_tree_dfs(root):
    path = []

    def dfs_helper(node):
        if not node:
            return

        path.append(node.data)
        dfs_helper(node.left)
        dfs_helper(node.right)

    dfs_helper(root)
    print("Binary Tree DFS Traversal: " + " - ".join(path))


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []

    def add_edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)

        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def graph_bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        path = []

        while queue:
            current = queue.popleft()
            path.append(current)

            for neighbor in self.adj_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        print("Graph BFS Traversal: " + " - ".join(path))


    def graph_dfs(self, start_vertex):
        visited = set()
        path = []

        def dfs_helper(vertex):
            visited.add(vertex)
            path.append(vertex)

            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start_vertex)
        print("Graph DFS Traversal: " + " - ".join(path))


if __name__ == "__main__":
    print("=== ASSESSMENT 3.3: NON-LINEAR DATA STRUCTURE (LAST NAME: LATORZA) ===\n")


    root = TreeNode('T')
    root.left = TreeNode('O')
    root.right = TreeNode('L')
    root.left.left = TreeNode('Z')
    root.left.right = TreeNode('A')
    root.right.left = TreeNode('R')


    print("--- 1. BINARY TREE ---")
    binary_tree_bfs(root)
    binary_tree_dfs(root)

    print()


    g = Graph()

    letters = ['A', 'O', 'T', 'Z', 'R', 'L', ]

    for i in range(len(letters) - 1):
        g.add_edge(letters[i], letters[i + 1])

    print("--- 2. GRAPH ---")
    g.graph_bfs('L')
    g.graph_dfs('L')
