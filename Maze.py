import random
class Maze(object):
    def __init__(self, w, h):
        self.m_W = w
        self.m_H = h 
        self.m_Maze = {}

    def SetWay(self, f, t):
        self.SetOrderedWay(f, t)
        self.SetOrderedWay(t, f)
    
    def SetOrderedWay(self, f, t):
        f = str(f)
        if(not f in self.m_Maze):
            self.m_Maze[f] = []
        self.m_Maze[f].append(t)

    def HasPath(self, f, t):
        f = str(f)
        if(not f in self.m_Maze):
            return False
        return t in self.m_Maze[f]

    def GetVertex(self, x, y):
        return self.m_W * y + x

    def Print(self):
        str = ''
        for x in range(self.m_W):
            str += ' __'#' __' -> 11
        print(str)
        for y in range(self.m_H):
            str = ''
            for x in range(self.m_W):
                if(x != 0 and self.HasPath(self.GetVertex(x, y), self.GetVertex(x - 1, y))):
                    str += ' '#' '
                else:
                    str += '|'#'|'
                if(self.HasPath(self.GetVertex(x, y), self.GetVertex(x, y + 1))):
                    str += '  '#'  ' 
                else:
                    str += '__'#'__'
            print(str + '|')#'|'
        print('')

    def ToList(self):
        maze_list = [[0 for i in range(2*self.m_W+1)] for j in range(2*self.m_H+1)]
        count = 4
        for y in range(self.m_H):
            for x in range(self.m_W):
                if(x != 0 and self.HasPath(self.GetVertex(x, y), self.GetVertex(x - 1, y))):
                    maze_list[2*y+1][2*x] = 0
                    maze_list[2*y+2][2*x] = 1
                else:
                    maze_list[2*y+1][2*x] = 1
                    maze_list[2*y+2][2*x] = 1 # '|' sign
                if(self.HasPath(self.GetVertex(x, y), self.GetVertex(x, y + 1))):
                    if (random.random() > 0.8 and count > 0):
                        maze_list[2*y+1][2*x+1] = count+1
                        count -= 1
                else:
                    maze_list[2*y+1][2*x+1] = 0
                    maze_list[2*y+2][2*x+1] = 1 # '_' sign
            maze_list[2*y+1][2*self.m_W] = 1
            maze_list[2*y+2][2*self.m_W] = 1
        for x in range(2*self.m_W+1):
            maze_list[0][x] = 1
            maze_list[self.m_H*2][x] = 1
        return maze_list