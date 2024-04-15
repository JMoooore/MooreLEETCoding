from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def mark_adjacent(row_count, col_count):
            if grid[row_count][col_count] == '1':
                grid[row_count][col_count] = '2'
                if row_count > 0:
                    mark_adjacent(row_count - 1, col_count)
                if row_count < len(grid) - 1:
                    mark_adjacent(row_count + 1, col_count)
                if col_count > 0:
                    mark_adjacent(row_count, col_count - 1)
                if col_count < len(grid[0]) - 1:
                    mark_adjacent(row_count, col_count + 1)

            return



        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    # do BFS
                    islands += 1
                    mark_adjacent(i, j)

        return islands


if __name__ == '__main__':
    sol = Solution()
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    grid3 = [["1","1","1"],["0","1","0"],["1","1","1"]]
    print(sol.numIslands(grid1))
    print(sol.numIslands(grid2))
    print(sol.numIslands(grid3))
