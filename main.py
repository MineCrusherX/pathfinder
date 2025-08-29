import pygame
from world import World
from pathfinder import Pathfinder
from bot import Bot

CELL = 24
FPS = 30

def draw(screen, world, bot, path):
    screen.fill((30,30,30))
    rows, cols = world.rows, world.cols
    for r in range(rows):
        for c in range(cols):
            rect = pygame.Rect(c*CELL, r*CELL, CELL-1, CELL-1)
            if world.grid[r,c] == 0:
                pygame.draw.rect(screen, (200,200,200), rect)
            else:
                pygame.draw.rect(screen, (50,50,50), rect)
    # Рисуем путь
    for p in path:
        rect = pygame.Rect(p[1]*CELL, p[0]*CELL, CELL-1, CELL-1)
        pygame.draw.rect(screen, (100,220,100), rect)
    br = pygame.Rect(bot.pos[1]*CELL, bot.pos[0]*CELL, CELL-1, CELL-1)
    pygame.draw.rect(screen, (50,120,255), br)

def main():
    pygame.init()
    world = World.sample_world()
    start = (0,0)
    bot = Bot(world, start)
    pf = Pathfinder(world)

    screen = pygame.display.set_mode((world.cols*CELL, world.rows*CELL))
    clock = pygame.time.Clock()

    goal = (world.rows-1, world.cols-1)
    path = pf.a_star(start, goal)
    bot.set_path(path)

    running = True
    auto = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                c = mx // CELL
                r = my // CELL
                if world.in_bounds((r,c)):
                    goal = (r,c)
                    path = pf.a_star(bot.pos, goal)
                    bot.set_path(path)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bot.step()
                    path = pf.a_star(bot.pos, goal)
                    bot.set_path(path)
                elif event.key == pygame.K_a:
                    auto = not auto
        if auto:
            bot.step()
            path = pf.a_star(bot.pos, goal)
            bot.set_path(path)

        draw(screen, world, bot, path)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
