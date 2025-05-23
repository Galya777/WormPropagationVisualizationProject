from collections import deque

graph = {
    1: [2, 3],
    2: [4],
    3: [],
    4: []
}

def dfs(node, visited):
    visited.add(node)
    print(node, end=' ')
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

def bfs(start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Пример:
dfs(1, set())
print()
bfs(1)
