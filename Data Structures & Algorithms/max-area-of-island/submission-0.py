class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1 # once the edge case testing is passsed it's confirmed that the area is 1
            for dr, dc in directions:
                area += dfs(r + dr, c + dc) # sums the area of all the '1' cells connected together

            return area

        rows = len(grid)
        cols = len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        maxArea = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    maxArea = max(maxArea, area)

        return maxArea

'''
For counting number of islands it was enough to keep a track of the count from the outside every time '1' was encountered but when Max area is required all the dfs operations needs to be summed for every '1' encountered to calculate the total number of '1' cells connected together and it is compared once out of the loop to check whether it is the highest possible value
'''