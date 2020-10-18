"""
Author : Qi
Date : 2020/10/18
"""


class Solution:
    # 逆流而上 从边缘往地势高的地方标记
    def pacificAtlantic(self, matrix):
        height, width = len(matrix), len(matrix[0])
        pacific = [[False] * width for _ in range(height)]  # 太平洋
        atlantic = [[False] * width for _ in range(height)]  # 大西洋
        for i in range(width):  # 矩阵上下
            self.__dfs(matrix, 0, i, pacific, matrix[0][i], height, width)
            self.__dfs(matrix, height - 1, i, atlantic, matrix[height - 1][i], height, width)
        for i in range(height):  # 矩阵左右
            self.__dfs(matrix, i, 0, pacific, matrix[i][0], height, width)
            self.__dfs(matrix, i, width - 1, atlantic, matrix[i][width - 1], height, width)
        ret = []
        for i in range(height):
            for j in range(width):
                if pacific[i][j] + atlantic[i][j] == 2:  # 太平洋和大西洋中都为True则添加到ret中
                    ret.append([i, j])
        return ret

    def __dfs(self, matrix, x, y, li, pre, height, width):
        if x < 0 or x > height - 1 or y < 0 or y > width - 1 or li[x][y] or matrix[x][y] < pre:
            # 边缘、已标记、地势比前一个低则跳出
            return
        li[x][y] = True
        self.__dfs(matrix, x + 1, y, li, matrix[x][y], height, width)
        self.__dfs(matrix, x - 1, y, li, matrix[x][y], height, width)
        self.__dfs(matrix, x, y + 1, li, matrix[x][y], height, width)
        self.__dfs(matrix, x, y - 1, li, matrix[x][y], height, width)


if __name__ == '__main__':
    tempList = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    s = Solution()
    print(s.pacificAtlantic(tempList))
