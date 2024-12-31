#this will allow us to use code from 
#the open-source pygame library
# throughout this file 

import pygame 
from constants import *



def main():
    
    print("Starting asteroids!")
    pygame.init() #used to initialize the game 
    time_clock = pygame.time.Clock()
    dt = 0 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True: 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        screen.fill((0,0,0))
        pygame.display.flip()
        dt = time_clock.tick(60)/1000 #pause the game loop until 1/60th of a second has passed


if __name__ == "__main__": 
    main()

