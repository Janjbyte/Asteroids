import pygame
from constants import *
from player import Player



def main():
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        time = pygame.time.Clock()
        
        # Groups the sprites together
        drawable = pygame.sprite.Group()
        updatable = pygame.sprite.Group()
        
        Player.containers = (updatable, drawable)
        
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        dt = 0
        

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   return
            
            # Added controls to sprite
            updatable.update(dt)    
            
            screen.fill(0)

            # Calling group
            for sprite in drawable:
                sprite.draw(screen)
            
            pygame.display.flip()
            
            # FPS limit 60
            dt = time.tick(60) / 1000
            

if __name__ == "__main__":
    main()