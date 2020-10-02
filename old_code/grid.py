"""
City is represented with an m*n grid.
It consists of b*b buildings seperated by r parking spaces, 2r roads.
"""
class Grid():
    def __init__(self, m = 1, n = 1, b = 1):
        self.grid = self.create_grid(m, n, b)
    
    def __str__(self):
        g_str = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                g_str += str(self.grid[i][j]) + " "
            g_str += "\n"
        g_str = g_str[:len(g_str) - 1]
        return g_str
    
    def __getitem__(self, key):
        (k1, k2) = key
        return self.grid[k2][k1]
    
    def get(self, k1, k2):
        return self.grid[k2][k1]

    def __setitem__(self, key, item):
        (k1, k2) = key
        self.grid[k2][k1] = item
    
    def create_grid(self, m, n, b):
        # M x N grid 
        grid = [[0 for _ in range(m)] for _ in range(n)]
        t = b + 4

        for i in range(m):
                for j in range(n):
                    
                    # Building
                    if(i % t <= b-1 and j % t <= b-1):
                        grid[i][j] = "#"
                    
                    # Traffic Light
                    elif((i % t == b and j % t == b)
                        or (i % t == b+3 and j % t == b+3)
                        or (i % t == b and j % t == b+3)
                        or (i % t == b+3 and j % t == b)):
                        grid[i][j] = 1
                    
                    # Parking Spot
                    elif((i % t == b and j % t < b)
                        or (i % t < b and j % t == b)
                        or (i % t < b and j % t == b+3)
                        or (i % t == b+3 and j % t <= b)):
                        grid[i][j] = 2
                    
                    # Intersection
                    elif((i % t == b + 2 and j % t == b + 2)
                        or (i % t == b+1 and j % t == b+1)
                        or (i % t == b+1 and j % t == b + 2)
                        or (i % t == b + 2 and j % t == b+1)):
                        grid[i][j] = "x"
                    
                    # East Road
                    elif(i % t == b + 2):
                        grid[i][j] = ">"

                    # North Road
                    elif(j % t == b + 2):
                        grid[i][j] = "^"
                    
                    # West Road
                    elif(i % t == b+1):
                        grid[i][j] = "<"
                    
                    # South Road
                    elif(j % t == b+1):
                        grid[i][j] = "v"
        return grid





