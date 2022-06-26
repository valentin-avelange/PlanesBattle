import pygame
from missile import *
import time 

class Plane(pygame.sprite.Sprite):
    def __init__(self, pos, speed, img, missile_img):
        pygame.sprite.Sprite.__init__(self)

        self.pos = pos
        self.speed = speed
        self.angle_speed = 3.5
        self.scale = 0.5
        self.can_fire = True

        self.image_origin = img
        self.missile_img = missile_img
        self.missile_timer = 0.3
        self.start_time = 0

        self.rotation = 0
        self.direction = pygame.math.Vector2(0, 1)

        self.image = img
        self.rect = self.image.get_rect()

    def update(self):
        self.image = pygame.transform.rotozoom(self.image_origin, self.rotation, self.scale)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        if time.time() - self.start_time > self.missile_timer:
            self.can_fire = True

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
        if self.can_fire:
            self.can_fire = False
            self.start_time = time.time()
            return Missile(self.pos, (self.direction.x, self.direction.y), 15, self.missile_img)