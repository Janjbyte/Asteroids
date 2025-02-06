import pygame
from constants import *
from circleshape import *
from player import *



def main():
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        time = pygame.time.Clock()
        dt = 0

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   return
                
            screen.fill(0)
            player.draw(screen)
            player.draw(screen)
            pygame.display.flip()
            
            # FPS limit 60
            dt = time.tick(60) / 1000
            

if __name__ == "__main__":
    main()