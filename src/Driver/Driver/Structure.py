from Attackable import *

class Structure(Attackable, object):
    def __init__(self, **kwds):
        super(Structure, self).__init__(**kwds)
    
class Nexus(Structure):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.atk = 0

class Tower(Structure, object):
    def __init__(self, **kwds):
        super(Tower, self).__init__(**kwds)

    def lockTarget(self, Game):
        for i in Game.PT.players:
            if self.distance(i) <= self.atkRange and self.alliance != i.alliance:
                # print(self.distance(i))
                # print(self.atkRange)
                # print(i)
                self.target = i
                break
            else:
                self.target = None
        # print(i)
    
    def defaultAttack(self, Game):
        if(self.atkCooldown <= 0 and self.target != None):
            if(self.atkType == "ranged"):
                self.projectileAttack(Game, self.target)
            else:
                self.basicAttack(Game.PT.players[i])
            self.atkCooldown += 60 / self.atkSpeed    
        elif(self.atkCooldown > 0):
            self.atkCooldown -= 1  
    
    def drawStructure(self):
        if(self.alliance == "a"):
            fill(0,0,255)
        elif(self.alliance == "b"):
            fill(255,0,0)
        else:
            fill(0,255,0)
        rect(self.x - self.wd/2,self.y - self.ht/2, self.wd, self.ht)
        #draw range
        noFill()
        if(self.alliance == "a"):
            stroke(0,0,255)
        elif(self.alliance == "b"):
            stroke(255,0,0)
        else:
            stroke(0,255,0)
        circle(self.x, self.y, self.atkRange * 2)
        noStroke()
        self.drawHealth()
