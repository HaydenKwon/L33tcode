//Not much to say
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[0]*m]*n
        for i in range(0,n):
            grid[i][0] = 1
        for j in range(0,m):
            grid[0][j] = 1
        for i in range(1,n):
            for j in range(1, m):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[n-1][m-1]
