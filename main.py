import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

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
    Player.containers = (updatable, drawable)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    while True:
        log_state()
        for event in pygame.event.get():
            pass
        screen.fill("black", rect=None, special_flags=0)
        updatable.update(dt)
        for objects in drawable:
            objects.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
        



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


            
if __name__ == "__main__":
     main()
