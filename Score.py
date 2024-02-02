import pygame

class Score:
    def __init__(self, score):
        self.score = score
        self.text = f'Score: {score}'
        self.font = pygame.font.SysFont('Comic Sans MS', 36)

    def render_font(self):
        return self.font.render(self.text, False, (255, 255, 255))

    def update_score(self, score):
        self.text = f'Score: {score}'

