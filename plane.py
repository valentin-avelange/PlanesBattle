import pygame
from missile import *

class Plane(pygame.sprite.Sprite):
    def __init__(self, pos, speed, img, missile_img):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pos
        self.speed = speed
        self.angle_speed = 3.5
        self.scale = 0.5

        self.image_origin = img
        self.missile_img = missile_img

        self.rotation = 0
        self.direction = pygame.math.Vector2(0, 1)

        self.image = img
        self.rect = self.image.get_rect()

    def update(self):
        self.image = pygame.transform.rotozoom(self.image_origin, self.rotation, self.scale)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def move(self, x_axis, y_axis):
        delta_rot = x_axis*self.angle_speed
        self.rotation -= delta_rot

        vec = pygame.math.Vector2(0, 1)
        vec.y = y_axis
        vec.rotate_ip(-self.rotation)

        self.direction.rotate_ip(delta_rot)
        self.direction.normalize_ip()

        self.pos = (self.pos[0] + vec.x, self.pos[1] + vec.y)

    def fire(self):
        return Missile(self.pos, (self.direction.x, self.direction.y), 15, self.missile_img)