import pygame
import sys
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Snake Game')

    game = Game(screen)
    game.start_game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            game.handle_input(event)

        game.update()
        game.draw()
        pygame.display.flip()
        pygame.time.Clock().tick(15)

if __name__ == "__main__":
    main()