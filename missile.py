import pygame 

class Missile(pygame.sprite.Sprite):
    def __init__ (self, pos, direction, speed, img):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pos
        self.direction = pygame.math.Vector2(direction[0], direction[1])
        self.speed = speed
        self.img = img
        self.scale = 0.25

        self.rotation = self.direction.angle_to(pygame.math.Vector2(0, 1))
        self.image = pygame.transform.rotozoom(self.img, self.rotation, self.scale)
        self.rect = self.image.get_rect()

    def update(self):
        self.pos = [self.pos[0] - self.speed*self.direction[0], self.pos[1] - self.speed*self.direction[1]]
        self.rect.center = self.pos