#this will allow us to use code from 
#the open-source pygame library
# throughout this file 
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable,drawable,shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)
            

        
        #for obj in asteroids: 
            #if obj.collision_detection(player):
                #print("Game over!")
               #sys.exit()
        #asteroid_bullet_collisions = pygame.sprite.groupcollide(asteroids, shots, True, True)
        #asteroid_player_collision = pygame.sprite.spritecollide(player, asteroids, False)

        for obj in asteroids: 
            
            if  obj.collision_detection(player):
                print("Game over!")
                sys.exit()
            for bullets in shots: 
                #print(f"Checking bullet collision: {bullets.position}")
                if bullets.collision_detection(obj):
                    obj.split()
                    bullets.kill()




        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
