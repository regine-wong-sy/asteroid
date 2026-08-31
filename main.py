import pygame, sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from circleshape import CircleShape
def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black", rect=None, special_flags=0)
        updatable.update(dt)
        for objects in asteroids:
            if objects.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for objects in asteroids:
            for shot in shots:
                if shot.collides_with(objects):
                    log_event("asteroid_shot")
                    pygame.sprite.Sprite.kill(shot)
                    objects.split()

        for objects in drawable:
            objects.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


            
if __name__ == "__main__":
     main()
