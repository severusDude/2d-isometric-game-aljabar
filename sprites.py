import pygame
import math
import random
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(COLOR_RED)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.collide_Blocks("x")
        self.collide_Blocks("y")
        pass

    def collide_Blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom


class Blocks(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(COLOR_BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


class Attack(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.attacks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x
        self.y = y
        self.width = TILE_SIZE
        self.height = TILE_SIZE

        self.animation_loop = 0
        self.image = self.game.attack_spritesheet.get_sprite(
            0, 0, self.width, self.height
        )
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.animate()
        self.collide()

    def collide(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, True)

    def animate(self):
        direction = self.game.player.facing

        right_animations = [
            self.game.attack_spritesheet.get_sprite(0, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(32, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(96, 64, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 64, self.width, self.height),
        ]

        down_animations = [
            self.game.attack_spritesheet.get_sprite(0, 32, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(32, 32, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 32, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(96, 32, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 32, self.width, self.height),
        ]

        left_animations = [
            self.game.attack_spritesheet.get_sprite(0, 96, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(32, 96, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 96, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(96, 96, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 96, self.width, self.height),
        ]

        up_animations = [
            self.game.attack_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(32, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(64, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(96, 0, self.width, self.height),
            self.game.attack_spritesheet.get_sprite(128, 0, self.width, self.height),
        ]

        if direction == "up":
            self.image = up_animations(math.floor(self.animation_loop))
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        if direction == "down":
            self.image = down_animations(math.floor(self.animation_loop))
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        if direction == "left":
            self.image = left_animations(math.floor(self.animation_loop))
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
        if direction == "right":
            self.image = right_animations(math.floor(self.animation_loop))
            self.animation_loop += 0.5
            if self.animation_loop >= 5:
                self.kill()
