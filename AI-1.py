from collections import deque

def dfs(graph, vertex, visited):
    if vertex not in visited:
        print(vertex, end=' ')
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

def recursive_bfs(graph, start, queue, visited):
    if not queue:
        return

    vertex = queue.popleft()
    print(vertex, end=' ')

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)

    recursive_bfs(graph, start, queue, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("\nBFS Traversal:")
    recursive_bfs(graph, start, queue, visited)

def main():
    graph = {}
    
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        src, dest = input("Enter edge (source destination): ").split()
        if src not in graph:
            graph[src] = []
        if dest not in graph:
            graph[dest] = []
        graph[src].append(dest)
        graph[dest].append(src)

    start_vertex = input("Enter the starting vertex: ")

    visited = set()

    print("\nDFS Traversal:")
    dfs(graph, start_vertex, visited)

    visited = set()

    bfs(graph, start_vertex)

if __name__ == "__main__":
    main()
