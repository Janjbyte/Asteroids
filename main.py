import pygame
from constants import *



def main():
        pygame.init()

        time = pygame.time.Clock()
        dt = 0
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   return
            screen.fill(0)
            pygame.display.flip()
            dt = time.tick(60)
            

if __name__ == "__main__":
    main()