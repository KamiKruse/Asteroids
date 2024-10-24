import sys
import pygame
from constants import *
from player import Player 
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = ( asteroid_group, updateable, drawable )
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    clock = pygame.time.Clock()
    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")

        for drawables in drawable:
            drawables.draw(screen)
    
        for updateables in updateable:
            updateables.update(dt)

        for obj in asteroid_group:
            for shot_obj in shots:
                if obj.collisioncheck(shot_obj):
                    obj.split()
                    shot_obj.kill()
            if obj.collisioncheck(player):
                print("Game Over!")
                sys.exit()

        pygame.display.flip()
        delta_time = clock.tick(60)
        dt = delta_time / 1000


if __name__ == "__main__":
    main()
