class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # DFS approach

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0': # testing for edge cases
                return 
            grid[r][c] = '0' # sinking the island once checked
            for dr,dc in directions:
                dfs(r + dr, c + dc)

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)

        return count