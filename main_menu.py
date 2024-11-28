import pygame
import sys
from main import Game # Impor game_loop dari game.py

# Inisialisasi Pygame
pygame.init()

# Konfigurasi Layar
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu and Game")

# Warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)

# Font
font = pygame.font.Font(None, 50)

# Opsi Menu
menu_options = ["Start Game", "Options", "Quit"]
selected_option = 0

def draw_menu():
    screen.fill(WHITE)
    title_text = font.render("Main Menu", True, BLACK)
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

    for i, option in enumerate(menu_options):
        color = BLUE if i == selected_option else BLACK
        text = font.render(option, True, color)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 200 + i * 60))

def main():
    global selected_option
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:  # Pilih opsi
                    if selected_option == 0:  
                       game_selection = Game 
                       game_selection.main
                       
                    elif selected_option == 1:  # Options
                        print("Options Menu (not implemented)")
                    elif selected_option == 2:  # Quit
                        pygame.quit()
                        sys.exit()

        draw_menu()
        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()