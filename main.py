import pygame
from constants import *
from player import Player



def main():
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        time = pygame.time.Clock()
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        dt = 0

        
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   return
            
            # Added controls to sprite
            Player.update(player, dt)    
            
            screen.fill(0)
            player.draw(screen)
            
            pygame.display.flip()
            
            # FPS limit 60
            dt = time.tick(60) / 1000
            

if __name__ == "__main__":
    main()