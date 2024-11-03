import math
import pygame
from pygame.locals import *

TILE_SIZE = 32
TILE_WIDTH = 64   # Lebar setiap tile
TILE_HEIGHT = 32  # Tinggi setiap tile
GRID_WIDTH = 10   # Lebar grid dalam jumlah tile
GRID_HEIGHT = 10  # Tinggi grid dalam jumlah tile


# Inisialisasi Pygame
pygame.init()

# Pengaturan jendela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Isometric 2D Physics Engine")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Player:
    def __init__(self, grid_x, grid_y):
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.pixel_position = grid_to_isometric(
            grid_x, grid_y)  # Awal posisi dalam isometrik

    def move(self, dx, dy):
        # Update posisi dalam grid (hanya satu tile per input)
        self.grid_x += dx
        self.grid_y += dy
        self.pixel_position = grid_to_isometric(self.grid_x, self.grid_y)


def grid_to_isometric(grid_x, grid_y):
    iso_x = (grid_x - grid_y) * TILE_WIDTH // 2
    iso_y = (grid_x + grid_y) * TILE_HEIGHT // 2
    return (iso_x + WIDTH // 2, iso_y + HEIGHT // 4)


def draw_grid():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            screen_position = grid_to_isometric(x, y)
            pygame.draw.polygon(
                screen, BLACK,
                [
                    (screen_position[0], screen_position[1]),  # top
                    (screen_position[0] + TILE_WIDTH // 2,
                     screen_position[1] + TILE_HEIGHT // 2),  # right
                    (screen_position[0], screen_position[1] + \
                     TILE_HEIGHT),  # bottom
                    (screen_position[0] - TILE_WIDTH // 2,
                     screen_position[1] + TILE_HEIGHT // 2)  # left
                ],
                1
            )


# Waktu per frame
clock = pygame.time.Clock()
running = True


# Pengaturan objek
MOVE_DELAY = 200  # Delay dalam milidetik
last_move_time = pygame.time.get_ticks()  # Timestamp terakhir gerakan

# Objek
player = Player(5, 5)  # Awal posisi pemain di grid


while running:
    dt = clock.tick(60) / 1000
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Menangani input keyboard untuk gerakan grid-based
    keys = pygame.key.get_pressed()
    if current_time - last_move_time > MOVE_DELAY:
        if keys[K_LEFT]:
            player.move(-1, 0)
            last_move_time = current_time
        elif keys[K_RIGHT]:
            player.move(1, 0)
            last_move_time = current_time
        elif keys[K_UP]:
            player.move(0, -1)
            last_move_time = current_time
        elif keys[K_DOWN]:
            player.move(0, 1)
            last_move_time = current_time

    # Gambar ulang semua objek
    screen.fill(WHITE)

    # Gambar grid sebagai ground
    draw_grid()

    pygame.draw.circle(screen, BLACK, player.pixel_position, 10)

    pygame.display.flip()

pygame.quit()
