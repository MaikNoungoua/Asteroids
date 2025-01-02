import pygame
from constants import SHOT_RADIUS

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_detection(self, other):
       distance = pygame.math.Vector2.distance_to(self.position, other.position)
       total_radius = self.radius + other.radius
       #print(f"Object types: {type(self)} and {type(other)}")
       #print(f"Distance: {distance}, Combined Radius: {total_radius}")
       return distance <= total_radius


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x,y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)


    