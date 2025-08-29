from queue import PriorityQueue
from typing import List, Tuple

def manhattan(a:Tuple[int,int], b:Tuple[int,int]) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

class Pathfinder:
    def __init__(self, world):
        self.world = world

    def neighbors(self, pos:Tuple[int,int]):
        r,c = pos
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < self.world.rows and 0 <= nc < self.world.cols:
                # Проходимая ячейка считается 0
                yield (nr,nc)

    def a_star(self, start:Tuple[int,int], goal:Tuple[int,int]) -> List[Tuple[int,int]]:
        if not self.world.in_bounds(start) or not self.world.in_bounds(goal):
            return []
        frontier = PriorityQueue()
        frontier.put((0, start))
        came_from = {start: None}
        cost_so_far = {start: 0}

        while not frontier.empty():
            current = frontier.get()[1]
            if current == goal:
                break
            for nxt in self.neighbors(current):
                if not self.world.is_passable(nxt):
                    continue
                new_cost = cost_so_far[current] + 1
                if nxt not in cost_so_far or new_cost < cost_so_far[nxt]:
                    cost_so_far[nxt] = new_cost
                    priority = new_cost + manhattan(nxt, goal)
                    frontier.put((priority, nxt))
                    came_from[nxt] = current
        if goal not in came_from:
            return []
        # Реконструкция пути
        path = []
        cur = goal
        while cur is not None:
            path.append(cur)
            cur = came_from.get(cur)
        path.reverse()
        return path
