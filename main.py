import pygame
from config import *
from sprites import *
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        # self.font = pygame.font.Font('Arial', 32)
        self.running = True

        self.character_spritesheet = Spritesheet(SPRITE_CHARACTER_FILE)
        self.terrain_spritesheet = Spritesheet(SPRITE_TERRAIN_FILE)

        self.attack_spritesheet = Spritesheet("img/attack.png")

    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Blocks(self, SPRITE_BLOCK_COORDS['semak'][0], j, i)
                if column == "S":
                    Blocks(self, random.choice(
                        SPRITE_BLOCK_COORDS['batu']), j, i)
                if column == "L":
                    Blocks(self, SPRITE_BLOCK_COORDS['lubang'][0], j, i)
                if column == "P":
                    self.player = Player(self, j, i)

    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTileMap()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == "up":
                        Attack(self, self.player.rect.x,
                               self.player.rect.y - TILE_SIZE)
                    if self.player.facing == "down":
                        Attack(self, self.player.rect.x,
                               self.player.rect.y + TILE_SIZE)
                    if self.player.facing == "left":
                        Attack(self, self.player.rect.x -
                               TILE_SIZE, self.player.rect.y)
                    if self.player.facing == "right":
                        Attack(self, self.player.rect.x +
                               TILE_SIZE, self.player.rect.y)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(COLOR_BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        """Game Loop"""
        while self.playing:
            self.events()
            self.update()
            self.draw()

        self.running = False

    def game_over(self):
        pass

    def intro_screen(self):
        pass


if __name__ == "__main__":
    g = Game()
    g.intro_screen()
    g.new()

    while g.running:
        g.main()

    pygame.quit()
    sys.exit()
