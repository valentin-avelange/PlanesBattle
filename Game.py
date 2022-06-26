import pygame
from pygame.locals import *
from plane import *

class Game:
    def __init__(self, res):
        self.res = res
        self.window_title = "WarPlane"
        self.is_running = True
        self.clock = pygame.time.Clock()

        self.player_plane_img = pygame.image.load("assets/warPlaneWhite.png")
        self.missile_img = pygame.image.load("assets/missiles/missile_red.png")

        self.player = Plane((200, 200), 10, self.player_plane_img, self.missile_img)

        self.player_missile_group = pygame.sprite.Group()

        self.start()

    def start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.res)
        pygame.display.set_caption(self.window_title)
        self.run()
    
    def run(self):
        while self.is_running:
            for evt in pygame.event.get():
                self.manage_events(evt)
            self.manage_pressed_keys()
            self.update()
        self.quit()

    def manage_events(self, evt):
        if evt.type == QUIT:
            self.is_running = False
        
        if evt.type == KEYDOWN:
            if evt.key == K_SPACE:
                missile = self.player.fire()
                self.player_missile_group.add(missile)

    def manage_pressed_keys(self):
        pressed = pygame.key.get_pressed()

        vector = [0,0]
        vector[1] = 2.5
        if pressed[K_UP] or pressed [K_z]:
            vector[1] = 5
        if pressed[K_DOWN] or pressed [K_s]:
            vector[1] = 1
        if pressed[K_LEFT] or pressed [K_q]:
            vector[0] = -1
        if pressed[K_RIGHT] or pressed [K_d]:
            vector[0] = 1

        self.player.move(vector[0], -vector[1])

    def draw(self):
        self.screen.blit(self.player.image, self.player.rect)
        self.player_missile_group.draw(self.screen)

    def update(self):
        self.screen.fill((48, 44, 52))

        self.player.update()

        self.player_missile_group.update()

        self.draw()

        self.clock.tick(120)
        pygame.display.update()
        

    def quit(self):
        pygame.display.quit()
        del self
