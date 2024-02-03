import pygame, os

class Wallpaper:
  def __init__(self, window_width, window_height):
    self.image_url = f'wallpaper.png'
    self.position_x = 0
    self.position_y = 0
    # self.rect = ''
    self.image = pygame.image.load(os.path.join('images', self.image_url))
    self.image = pygame.transform.scale(self.image, (window_width, window_height))

  def draw(self, window):
    # self.rect = pygame.Rect(self.position_x, self.position_y, 10, 10)
    window.blit(self.image, (self.position_x, self.position_y))