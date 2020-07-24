class Solution:
    def islandPerimeter(self, grid: list) -> int:
        H, W = len(grid), len(grid[0])
        area = 0
        connect = 0
        for r in range(H):
            for c in range(W):
                if grid[r][c] == 1:
                    area += 1
                    if r > 0 and grid[r - 1][c] == 1:
                        connect += 1
                    if c > 0 and grid[r][c - 1] == 1:
                        connect += 1
        return area * 4 - 2 * connect


test = [[0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0]]

a = Solution()
b = a.islandPerimeter(test)
print(b)
