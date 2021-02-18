from Maze import Maze
#from Qrandom import qrandom
import random

def qrandom():
    return bool(random.getrandbits(1))

class MazeGenerator(object):
    def __init__(self, w, h):
        self.m_W = max(1, w)
        self.m_H = max(1, h)
        self.Generate()

    def InitSet(self):
        self.m_LastSetNumber = 0 
        self.m_Set = []
        for i in range(self.m_W):
            self.m_LastSetNumber += 1
            self.m_Set.append(self.m_LastSetNumber)

    def DestroyLeftWalls(self, y):
        for x in range(1, self.m_W):
            if(self.m_Set[x] != self.m_Set[x - 1] and qrandom()):
                self.SetWay(x - 1, y, x, y)

    def DestroyDownLines(self, y):
        hasDownWay = False
        for x in range(self.m_W):
            if(qrandom()):
                self.SetWay(x, y, x, y + 1)
                hasDownWay = True
            if(x == self.m_W - 1 or self.m_Set[x] != self.m_Set[x + 1]):
                if(hasDownWay):
                    hasDownWay = False
                else:
                    self.SetWay(x, y, x, y + 1)

    def UpdateSet(self, y):
        for x in range(self.m_W):
            if(not self.HasPath(x, y, x, y + 1)):
                self.m_LastSetNumber += 1
                self.m_Set[x] = self.m_LastSetNumber

    def ProcessLastLine(self):
        y = self.m_H - 1
        for x in range(1, self.m_W):
            if(self.m_Set[x] != self.m_Set[x-1]):
                self.SetWay(x, y, x - 1, y)

    def Generate(self):
        self.m_Maze = Maze(self.m_W, self.m_H)  
        self.InitSet()
        for y in range(self.m_H - 1):   
            self.DestroyLeftWalls(y)
            self.DestroyDownLines(y)
            self.UpdateSet(y)
        self.ProcessLastLine()
        return self.m_Maze

    def MergeSet(self, x1, x2):
        setNumToReplace = max(self.m_Set[x1], self.m_Set[x2])
        newSetNum = min(self.m_Set[x1], self.m_Set[x2])
        for x in range(self.m_W):
            if(self.m_Set[x] == setNumToReplace):
                self.m_Set[x] = newSetNum

    def SetWay(self, x1, y1, x2, y2):
        self.m_Maze.SetWay(self.m_Maze.GetVertex(x1, y1), self.m_Maze.GetVertex(x2, y2))
        self.MergeSet(x1, x2)

    def HasPath(self, x1, y1, x2, y2):
        return self.m_Maze.HasPath(self.m_Maze.GetVertex(x1, y1), self.m_Maze.GetVertex(x2, y2))

    def GetMaze(self):
        return self.m_Maze

if __name__ == "__main__":
    print('maze size: m by n')
    m=int(input('m: '))
    n=int(input('n: '))
    mazeGenerator = MazeGenerator(m, n)
    maze = mazeGenerator.GetMaze()
    maze.Print()
    print(maze.ToList())