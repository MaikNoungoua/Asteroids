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
    pygame.font.init()
    pygame.mixer.init()


    my_font = pygame.font.SysFont('Arial', 30)
    background = pygame.image.load('./images/background1.jpg')
    score_value = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    asteroid_sound = pygame.mixer.Sound('./sounds/aste_destruction.wav')

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

    def printing_score(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))
    

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

        for obj in updatable:
            obj.update(dt)

        screen.blit(background, (0,0))
            

        for obj in asteroids: 
            
            if  obj.collision_detection(player):
                print("Game over!")
                sys.exit()
            for bullets in shots: 
                #print(f"Checking bullet collision: {bullets.position}")
                if bullets.collision_detection(obj):
                    pygame.mixer.Sound.play(asteroid_sound)
                    obj.split()
                    bullets.kill()
                    score_value += obj.update_score()
                    
                    print(f"new score = {score_value}")

        


        #screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        
        score_card = "Score = " + str(score_value)

        printing_score(str(score_card), my_font,(255,255,255), 1000, 650)

        pygame.display.update()
        #pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
