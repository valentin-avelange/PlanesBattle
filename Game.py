import pygame
from pygame.locals import *
from plane import *

class Game:
    def __init__(self, res):
        self.res = res

        self.bords = [ [-30, self.res[0] + 30], [-30, self.res[1] + 30] ]

        self.player_bords = [ [20, self.res[0] -20], [10, self.res[1] - 20] ]

        self.window_title = "WarPlane"
        self.is_running = True
        self.clock = pygame.time.Clock()

        self.player_plane_img = pygame.image.load("assets/warPlaneWhite.png")
        self.missile_img = pygame.image.load("assets/missiles/missile_white.png")

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
                if missile:
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

        #x
        if self.player.pos[0] < self.player_bords[0][0]:
            self.player.pos = (self.player_bords[0][0], self.player.pos[1]) 
        elif self.player.pos[0] > self.player_bords[0][1]:
            self.player.pos = (self.player_bords[0][1], self.player.pos[1])

        #y
        if self.player.pos[1] < self.player_bords[1][0]:
            self.player.pos = (self.player.pos[0], self.player_bords[1][0])
        if self.player.pos[1] > self.player_bords[1][1]:
            self.player.pos = (self.player.pos[0], self.player_bords[1][1])

    def draw(self):
        self.screen.blit(self.player.image, self.player.rect)
        self.player_missile_group.draw(self.screen)

    def clear_missile(self):
        for missile in self.player_missile_group.sprites():
            if missile.rect.centerx < self.bords[0][0] or missile.rect.centerx > self.bords[0][1]:
                self.player_missile_group.remove(missile)
            if missile.rect.centery < self.bords[1][0] or missile.rect.centery > self.bords[1][1]:
                self.player_missile_group.remove(missile)    
            if missile not in self.player_missile_group.sprites():
                print("missile deleted !")
                del missile

    def update(self):
        self.screen.fill((48, 44, 52))

        self.clear_missile()

        self.player.update()
        self.player_missile_group.update()

        self.draw()

        self.clock.tick(120)
        pygame.display.update()
        

    def quit(self):
        pygame.display.quit()
        del self
