from collections import deque

def is_valid(matrix, visited, row, col,current):
    n = len(matrix)
    m = len(matrix[0])
    return (row >= 0) and (row < n) and (col >= 0) and (col < m) and (matrix[row][col]+matrix[current[0]][current[1]] > 0) and not visited[row][col]

def shortest_path(start, end):
    matrix = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0]
    ]
    n = len(matrix)
    m = len(matrix[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    parent = {}

    while queue:
        current = queue.popleft()
        if current == end:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]  # Return the path in reverse to get it from start to end
        for direction in directions:
            row = current[0] + direction[0]
            col = current[1] + direction[1]
            if is_valid(matrix, visited, row, col, current):
                queue.append((row, col))
                visited[row][col] = True
                parent[(row, col)] = current

    return []

# Example usage

# start_point = (1, 0)
# end_point = (0, 0)

# path = shortest_path(matrix, start_point, end_point)
# if path:
#     print(f"There is a path from {start_point} to {end_point}")
#     print("The shortest path is:", path)
# else:
#     print(f"There is no path from {start_point} to {end_point}")
