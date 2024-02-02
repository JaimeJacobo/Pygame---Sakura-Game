import pygame, os, random

class Leaf:
  def __init__(self, position_x, position_y):
    self.image_url = f'leaf_{random.randint(1, 7)}.png'
    self.speed = random.uniform(0.3, 0.7)
    self.position_x = position_x
    self.position_y = position_y
    self.rect = ''
    self.image = pygame.image.load(os.path.join('images', self.image_url))
    self.image = pygame.transform.scale_by(self.image, 1)

  def draw(self, window):
    self.rect = pygame.Rect(self.position_x, self.position_y, 50, 50)
    window.blit(self.image, (self.position_x, self.position_y))

  def move(self):
    self.position_y += self.speed