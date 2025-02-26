def draw_snake(surface, snake_body, block_size):
    for block in snake_body:
        pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(block[0], block[1], block_size, block_size))

def draw_food(surface, food_position, block_size):
    pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(food_position[0], food_position[1], block_size, block_size))

def game_over(surface, score):
    font = pygame.font.SysFont('Arial', 50)
    game_over_surface = font.render('Game Over', True, (255, 255, 255))
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    surface.blit(game_over_surface, (surface.get_width() // 4, surface.get_height() // 4))
    surface.blit(score_surface, (surface.get_width() // 4, surface.get_height() // 4 + 50))
    pygame.display.flip()
    pygame.time.wait(2000)