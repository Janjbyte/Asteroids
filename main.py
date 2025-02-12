import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import *



def main():
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        time = pygame.time.Clock()
        
        # Groups the sprites together
        drawable = pygame.sprite.Group()
        updatable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        
        
        Player.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable)
        Shot.containers = (shots, updatable, drawable)
        
        asteroid_field = AsteroidField()
    
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        dt = 0
        

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   return
            
            # Added controls to sprite
            for obj in updatable: 
                obj.update(dt)
            
            for aster in asteroids:
                if aster.check_for_collision(player) == True:
                    sys.exit("Game over!")
                for shot in shots:
                    if aster.check_for_collision(shot) == True:
                       aster.split()
                       shot.kill()

                

            screen.fill(0)

            # Calling group
            for sprite in drawable:
                sprite.draw(screen)
            
            pygame.display.flip()
            
            # FPS limit 60
            dt = time.tick(60) / 1000
            

if __name__ == "__main__":
    main()