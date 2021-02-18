import json

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
#        MazeList = [[0 for i in range(2*m+1)] for j in range(2*n+1)]
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

    def ToJSON(self):
        return json.dumps({
            'Width': self.m_W,
            'Height': self.m_H,
            'Graph': self.m_Maze
            })

    def FromJSON(self, jsonString):
        data = json.loads(jsonString)
        self.m_W = data['Width']
        self.m_H = data['Height']
        self.m_Maze = data['Graph']