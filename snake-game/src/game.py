class Game:
    def __init__(self):
        self.snake_position = [(100, 50), (90, 50), (80, 50)]
        self.food_position = (0, 0)
        self.direction = 'RIGHT'
        self.score = 0
        self.game_over = False

    def start_game(self):
        self.generate_food()

    def generate_food(self):
        import random
        self.food_position = (random.randint(1, 19) * 10, random.randint(1, 19) * 10)

    def update(self):
        if not self.game_over:
            self.move_snake()
            self.check_collisions()

    def move_snake(self):
        head_x, head_y = self.snake_position[0]
        if self.direction == 'UP':
            head_y -= 10
        elif self.direction == 'DOWN':
            head_y += 10
        elif self.direction == 'LEFT':
            head_x -= 10
        elif self.direction == 'RIGHT':
            head_x += 10

        self.snake_position.insert(0, (head_x, head_y))
        if self.snake_position[0] == self.food_position:
            self.score += 1
            self.generate_food()
        else:
            self.snake_position.pop()

    def check_collisions(self):
        head_x, head_y = self.snake_position[0]
        if head_x < 0 or head_x >= 200 or head_y < 0 or head_y >= 200 or len(self.snake_position) != len(set(self.snake_position)):
            self.game_over = True

    def draw(self, surface):
        import pygame
        surface.fill((0, 0, 0))
        for segment in self.snake_position:
            pygame.draw.rect(surface, (0, 255, 0), pygame.Rect(segment[0], segment[1], 10, 10))
        pygame.draw.rect(surface, (255, 0, 0), pygame.Rect(self.food_position[0], self.food_position[1], 10, 10))