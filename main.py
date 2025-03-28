import pygame

from constants import *
from player import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Use pygame's display.set.mode() to get a new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create pygame clock
    pygame.time.Clock()
    dt = 0

    # Draw Player
    player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))

    # Create (infinite) game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill screen with solid black color
        screen.fill(0)

        # Check for movement
        player.update(dt)

        # at end of iteration, call .tick, pas 60 (pauses game loop until 1/60th of a second passes)
        pygame.time.Clock().tick(60)
        dt = pygame.time.Clock().tick(60) / 1000

        # re-render player
        player.draw(screen)

        # refresh screen (last thing in loop)
        pygame.display.flip()

if __name__ == "__main__":
    main()
