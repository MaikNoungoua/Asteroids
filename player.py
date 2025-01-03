import pygame
from circleshape import CircleShape , Shot
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, SHOT_RADIUS


class Player(CircleShape): 
    
    rotation = 0 
    
    def __init__ (self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.containers = ()
        self.timer = 0 
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,(255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt 

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.timer > 0:
            self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate((-dt))
            
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE] and self.timer <= 0:
            weapon_sound = pygame.mixer.Sound('./sounds/laser_se.wav')
            self.shoot()
            pygame.mixer.Sound.play(weapon_sound)
            self.timer = 0.3
            



    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        
        spawn_position = pygame.Vector2(self.position)
        

        shot = Shot(spawn_position.x, spawn_position.y)
        shot_direction = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = shot_direction * PLAYER_SHOOT_SPEED






