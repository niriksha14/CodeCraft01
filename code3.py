def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# New example graph:
graph = {
    'X': ['Y', 'Z'],
    'Y': ['P', 'Q'],
    'Z': ['R'],
    'P': [],
    'Q': ['R'],
    'R': []
}

dfs(graph, 'X')  
