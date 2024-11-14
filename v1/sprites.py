import pygame
from config import *
import math
import random


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0

        self.facing = "down"

        # menggambar player
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        # fungsi yang mengatur dari posisi awal player
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.rect.y += self.y_change
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        kesy = pygame.key.get_pressed()
        if kesy[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = "left"
        if kesy[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = "right"
        if kesy[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = "up"
        if kesy[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = "down"


class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.bloks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
