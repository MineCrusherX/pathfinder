from typing import List, Tuple

class Bot:
    def __init__(self, world, start:Tuple[int,int]):
        self.world = world
        self.pos = start
        self.path = []
        self.actions = []

    def set_path(self, path:List[Tuple[int,int]]):
        self.path = path
        self.actions = self.path_to_actions(path)

    def path_to_actions(self, path:List[Tuple[int,int]]):
        # Преобразуем последовательность координат в простые действия.
        actions = []
        if not path or len(path) < 2:
            return actions
        cur = path[0]
        for nxt in path[1:]:
            dr = nxt[0] - cur[0]
            dc = nxt[1] - cur[1]
            if dr == -1 and dc == 0:
                actions.append('move_up')
            elif dr == 1 and dc == 0:
                actions.append('move_down')
            elif dr == 0 and dc == -1:
                actions.append('move_left')
            elif dr == 0 and dc == 1:
                actions.append('move_right')
            else:
                actions.append('unknown')
            if not self.world.is_passable(nxt):
                actions.append('mine_block')
            cur = nxt
        return actions

    def step(self):
        if not self.actions:
            return
        act = self.actions.pop(0)
        if act == 'move_up':
            self.pos = (self.pos[0]-1, self.pos[1])
        elif act == 'move_down':
            self.pos = (self.pos[0]+1, self.pos[1])
        elif act == 'move_left':
            self.pos = (self.pos[0], self.pos[1]-1)
        elif act == 'move_right':
            self.pos = (self.pos[0], self.pos[1]+1)
        elif act == 'mine_block':
            r,c = self.pos
            for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < self.world.rows and 0 <= nc < self.world.cols and not self.world.is_passable((nr,nc)):
                    self.world.remove_block((nr,nc))
                    break
        else:
            pass
