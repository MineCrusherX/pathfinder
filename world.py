from typing import List, Tuple
import numpy as np

class World:
    def __init__(self, rows:int=20, cols:int=30):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=int)

    def in_bounds(self, pos:Tuple[int,int]) -> bool:
        r,c = pos
        return 0 <= r < self.rows and 0 <= c < self.cols

    def is_passable(self, pos:Tuple[int,int]) -> bool:
        r,c = pos
        return self.grid[r,c] == 0

    def set_block(self, pos:Tuple[int,int], value:int=1):
        r,c = pos
        if self.in_bounds(pos):
            self.grid[r,c] = value

    def remove_block(self, pos:Tuple[int,int]):
        self.set_block(pos, 0)

    @staticmethod
    def sample_world():
        w = World(20, 30)
        for r in range(5,15):
            w.set_block((r,10))
        for c in range(12,25):
            w.set_block((12,c))
        for c in range(5,9):
            w.set_block((16,c))
            w.remove_block((16,c))
        import random
        for _ in range(60):
            rr = random.randint(0, w.rows-1)
            cc = random.randint(0, w.cols-1)
            if (rr,cc) not in [(0,0),(w.rows-1,w.cols-1)]:
                w.set_block((rr,cc), 1 if random.random() < 0.5 else 0)
        for c in range(3,7):
            w.set_block((8,c), 1)
        return w
