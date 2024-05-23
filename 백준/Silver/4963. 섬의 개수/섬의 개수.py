def dfs(x, y, w, h, grid, visited):
    # 8방향 탐색 (상, 하, 좌, 우, 대각선)
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for direction in range(8):
            nx, ny = cx + dx[direction], cy + dy[direction]
            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and grid[ny][nx] == 1:
                visited[ny][nx] = True
                stack.append((nx, ny))

def count_islands(w, h, grid):
    visited = [[False] * w for _ in range(h)]
    island_count = 0
    
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 1 and not visited[y][x]:
                # 새로운 섬 발견
                visited[y][x] = True
                dfs(x, y, w, h, grid, visited)
                island_count += 1
                
    return island_count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    while idx < len(data):
        w = int(data[idx])
        h = int(data[idx + 1])
        if w == 0 and h == 0:
            break
        idx += 2
        grid = []
        for _ in range(h):
            row = list(map(int, data[idx:idx + w]))
            grid.append(row)
            idx += w
        print(count_islands(w, h, grid))

if __name__ == "__main__":
    main()
