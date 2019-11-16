import pygame
pygame.init()
game_window = pygame.display.set_mode((1200,500))
pygame.display.set_caption("my First game")

#creating game specific variables
game_exit = False
game_over = False

#creating game loop
while not game_exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You press right key")

pygame.quit()
quit()
