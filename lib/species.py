import random as r
class Species:
    def __init__(self):
        # illness=0 <=> sound
        # illness=100 <=> dead
        self.illness = 0 
        self.maxIll = 100
        self.maxX = 6000
        self.maxY = 6000
        self.x=round(self.maxX*r.random())
        self.y=round(self.maxY*r.random())

    def raiseInfection(self, amount):
        self.illness = self.illness+amount
        if self.illness >=100:
            self.illness = 100

    def getIllness(self):
        return (self.illness)

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def setX(self,x):
        self.x=x

    def setY(self,y):
        self.y=y

    def goToXY(self,x,y):
        self.x=x
        self.y=y

    def moveRandomly(self,dx=2,dy=2):
        #self.dx=round(dx*r.random())-0.5*dx
        #self.dy=round(dy*r.random())-0.5*dy
        self.dx=r.randint(-dx,dx)
        self.dy=r.randint(-dy,dy)
        # Reflective boundary condition here
        self.nx=self.x+self.dx
        self.ny=self.y+self.dy
        if (self.nx < 0 or self.nx > self.maxX):
            self.x = self.x - self.dx
        else:
            self.x=self.nx

        if (self.ny < 0 or self.ny > self.maxY):
            self.y = self.y - self.dy
        else:
            self.y=self.ny
