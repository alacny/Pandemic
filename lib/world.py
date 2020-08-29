class World:
    def __init__(self, h, xdim, ydim):
        self.xy = [] 
        for i in range(0,ydim):
            self.xy.append([i]*ydim)

        print (self.xy)
        
