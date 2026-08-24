class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        def bfs(x,y):
            q=[(x,y)]
            grid[x][y] ="0"
            comb = [(0,1), (0,-1), (1,0), (-1,0)]
            while q:

                x,y = q[0]
                q.pop(0)

                
                for c in comb: 
                    m = x+c[0]
                    n = y + c[1]
                    if m >=0 and m < len(grid) and n >= 0 and n < len(grid[0]) and grid[m][n] =="1":
                        q.append((m,n))
                        grid[m][n]="0"
           
        
        
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == "1":
                    print(grid[i][j])
                    count += 1
                    bfs(i,j)


        return count
        
        