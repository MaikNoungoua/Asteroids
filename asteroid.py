import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
     
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return 
        else: 
            asteroid_position = self.position
            random_angle = random.uniform(20,50)
            vector1 = pygame.Vector2(0, 1).rotate(random_angle)
            vector2 = pygame.Vector2(0, 1).rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(asteroid_position.x, asteroid_position.y, new_radius )
            ast2 = Asteroid(asteroid_position.x, asteroid_position.y, new_radius )
            ast1.velocity = vector1 * 50.2
            ast2.velocity = vector2 * 50.2
            #ast1 = Asteroid(self.position.x, self.position.y, new_radius )

    def update_score(self):
        
        if self.radius == 5 : 
            return 25
        elif self.radius == 20: 
            return 15
        elif self.radius == 40: 
            return 10
        elif self.radius == 60: 
            return 5
        

        


    

    
        

