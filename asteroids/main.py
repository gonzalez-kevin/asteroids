import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    # setting variables
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # instantiating player object in the middle of the screen

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # infinite loop closed by quitting the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0)) #creates black screen
        player.draw(screen) #draws 'triangle'(player) in the middle of the screen
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()

