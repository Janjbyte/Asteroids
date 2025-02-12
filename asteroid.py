import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        
        

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    # new method of splitting asteroids into smaller parts until they reach min radius
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_size = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        asteroid_1 = self.velocity.rotate(random_angle)
        asteroid_2 = self.velocity.rotate(-random_angle)

        
        new_asteroid = Asteroid(self.position.x, self.position.y, new_size)
        new_asteroid.velocity = asteroid_1 * 1.2
        new_asteroid = Asteroid(self.position.x, self.position.y, new_size)
        new_asteroid.velocity = asteroid_2 * 1.2