class Solution:
    def prisonAfterNDays(self, cells: list, N: int) -> list:
        act = N % 14
        if act == 0:
            act = 14
        for i in range(act):
            new_cell = [0, 0, 0, 0, 0, 0, 0, 0]
            for p, val in enumerate(cells):
                if p == 7 or p == 0:
                    continue
                if cells[p-1] == cells[p + 1]:
                    new_cell[p] = 1
                else:
                    new_cell[p] = 0
            cells = new_cell
        return cells


a = Solution()
b = a.prisonAfterNDays([1, 0, 0, 1, 0, 0, 0, 1], 826)
print(b)
