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
        self.animation_loop = 1

        # menggambar player
        self.image = self.game.characters_spritesheet.get_sprite(
            3, 2, self.width, self.height
        )

        # fungsi yang mengatur dari posisi awal player
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        # movement function
        self.movement()

        # animation function
        self.animate()

        # function end game if hit enemy
        self.collide_enemy()

        # mempengaruhi posisi objek dengan nilai yang sudah dibuat
        self.rect.x += self.x_change
        # membuat collision pada sumbu x
        self.collide_blocks("x")

        # mempengaruhi posisi objek dengan nilai yang sudah dibuat
        self.rect.y += self.y_change
        # membuat collision pada sumbu y
        self.collide_blocks("y")

        # restart change movement
        self.x_change = 0
        self.y_change = 0

    def movement(self):
        kesy = pygame.key.get_pressed()
        if kesy[pygame.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = "left"
        if kesy[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.x_change += PLAYER_SPEED
            self.facing = "right"
        if kesy[pygame.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.y_change -= PLAYER_SPEED
            self.facing = "up"
        if kesy[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.y_change += PLAYER_SPEED
            self.facing = "down"

    def collide_enemy(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.kill()
            self.game.playing = False

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

    def animate(self):
        down_animations = [
            self.game.characters_spritesheet.get_sprite(3, 2, self.width, self.height),
            self.game.characters_spritesheet.get_sprite(35, 2, self.width, self.height),
            self.game.characters_spritesheet.get_sprite(68, 2, self.width, self.height),
        ]

        up_animations = [
            self.game.characters_spritesheet.get_sprite(3, 34, self.width, self.height),
            self.game.characters_spritesheet.get_sprite(
                35, 34, self.width, self.height
            ),
            self.game.characters_spritesheet.get_sprite(
                68, 34, self.width, self.height
            ),
        ]

        left_animations = [
            self.game.characters_spritesheet.get_sprite(3, 98, self.width, self.height),
            self.game.characters_spritesheet.get_sprite(
                35, 98, self.width, self.height
            ),
            self.game.characters_spritesheet.get_sprite(
                68, 98, self.width, self.height
            ),
        ]

        right_animations = [
            self.game.characters_spritesheet.get_sprite(3, 66, self.width, self.height),
            self.game.characters_spritesheet.get_sprite(
                35, 66, self.width, self.height
            ),
            self.game.characters_spritesheet.get_sprite(
                68, 66, self.width, self.height
            ),
        ]

        if self.facing == "down":
            if self.y_change == 0:
                self.image = self.game.characters_spritesheet.get_sprite(
                    3, 2, self.width, self.height
                )
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "up":
            if self.y_change == 0:
                self.game.characters_spritesheet.get_sprite(
                    3, 34, self.width, self.height
                )
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0:
                self.game.characters_spritesheet.get_sprite(
                    3, 66, self.width, self.height
                )
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.characters_spritesheet.get_sprite(
                    3, 98, self.width, self.height
                )
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1


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


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        # restart change movement
        self.x_change = 0
        self.y_change = 0

        self.facing = random.choice(["left", "right"])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(20, 30)

        self.image = self.game.enemy_spritesheet.get_sprite(
            3, 2, self.width, self.height
        )
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        if self.facing == "left":
            self.x_change -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = "right"

        if self.facing == "right":
            self.x_change += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = "left"

    def animate(self):
        left_animations = [
            self.game.enemy_spritesheet.get_sprite(3, 98, self.width, self.height),
            self.game.enemy_spritesheet.get_sprite(35, 98, self.width, self.height),
            self.game.enemy_spritesheet.get_sprite(68, 98, self.width, self.height),
        ]

        right_animations = [
            self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height),
            self.game.enemy_spritesheet.get_sprite(35, 66, self.width, self.height),
            self.game.enemy_spritesheet.get_sprite(68, 66, self.width, self.height),
        ]

        if self.facing == "right":
            if self.x_change == 0:
                self.game.enemy_spritesheet.get_sprite(3, 66, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0:
                self.image = self.game.enemy_spritesheet.get_sprite(
                    3, 98, self.width, self.height
                )
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
