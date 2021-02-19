# import qiskit
import random
class Maze:
    def __init__(self):
       self.M = 10
       self.N = 8
       self.maze = [ [1,1,1,1,1,1,1,1,1,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,0,1,1,1,1,1,1,0,1],
                     [1,0,1,0,0,0,0,0,0,1],
                     [1,0,1,0,1,1,1,1,0,1],
                     [1,0,0,0,0,0,0,0,0,1],
                     [1,1,1,1,1,1,1,1,1,1],]

    def update(self):
        # 얽힌 벽이라던지 만날때 self.maze 업데이트 용
        pass

    def get_solution(self):
        return SearchWall.search(self.maze)

    def entangle(self, wall1, wall2):
        pass

    def makeEntangledWall(self):
        # 1. 현재 미로 가져오기
        currentEscapePath = self.get_solution()
        # 2. 탈출 경로 중간에 벽을 만들어 경로를 끊는다(이하 얽힘 벽)
        index = random.randint(1, len(currentEscapePath))
        # 3. 기존 탈출 경로와 얽힘 벽 이후 탈출 경로를 저장한다.
        prev_esc_path = currentEscapePath[:index]
        after_esc_path = currentEscapePath[index:]
        # 5. 벽을 사이에 두고 1과 2가 만나는 벽을 리스트에 추가한다.
        location = (0,0)
        walls_meet = []
        for step in currentEscapePath:
            location = location[0]+path[0], location[1]+path[1]
            if (location[0]+1, location[1]) in after_esc_path or (location[0]-1, location[1]) in after_esc_path or (location[0], location[1]+1) in after_esc_path or (location[0], location[1]-1) in after_esc_path:
                # 벽 구현 방법은 알아서 고민하세용
                #이거 표현형이 벽이 아니라 점을 구현하는거라 1. 점을 기둥으로 생각하기(좌표 저장) 2.표현형 바꾸기(종만이한테 설명했었음)를  
                walls_meet.append(location)

        # 6. 리스트에서 하나의 벽을 꺼내서 얽힘 벽과 양자얽힘 상태를 만든다.
        wall_to_entangle = random.choice(walls_meet)

        # self.ENTANGLE(wall_to_entangle, currentEscapePath[index])
class SearchWall:
    def search(self):
        # 4. 나머지 미로를 탐사한다.
        return [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
