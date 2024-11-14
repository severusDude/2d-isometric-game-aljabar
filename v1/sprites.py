import pygame
from config import *
import math
import random


class Spritesheet:
    """
    function for access image or asset for this gane
    """

    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite


class Player(pygame.sprite.Sprite):
    """
    function for create sprite Player
    """

    def __init__(self, game, x, y):

        # inisiasi pembuatan tururan dari game
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        # mengatur nilai awal
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # nilai yang akan mempengaruhi movement player
        self.x_change = 0
        self.y_change = 0

        self.facing = "down"

        # menggambar player
        self.image = self.game.characters_spritesheet.get_sprite(
            3, 2, self.width, self.height
        )

        # fungsi yang mengatur dari posisi awal player
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')
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

    # function for colletion
    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.bloks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.bloks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom


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

        self.image = self.game.terrain_spritesheet.get_sprite(
            960, 448, self.width, self.height
        )

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(
            64, 352, self.width, self.height
        )

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
