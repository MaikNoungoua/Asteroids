#this will allow us to use code from 
#the open-source pygame library
# throughout this file 

import pygame 
from constants import *
from player import Player



def main():
    
    print("Starting asteroids!")
    pygame.init() #used to initialize the game 
    time_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0 

    while True: 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        player.update(dt)
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip()
        #limit the framerate to 60 FPS
        dt = time_clock.tick(60) / 1000


if __name__ == "__main__": 
    main()

