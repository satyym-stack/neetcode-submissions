from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        island = 0
        def bfs(row, col):
            queue = deque([(row, col)])
            visited.add((row, col))

            while queue:
                node = queue.popleft()
                r,c = node
                directions = [
                    (-1, 0), # up 
                    (1, 0), # down
                    (0, -1), # left
                    (0, 1) # right
                ]
                for dr, dc in directions:
                    new_row = r + dr
                    new_col = c + dc

                    if 0<= new_row < rows and 0<= new_col < cols and grid[new_row][new_col] == "1" and (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    island += 1
                    bfs(r,c )
        
        return island