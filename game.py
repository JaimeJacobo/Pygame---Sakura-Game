import pygame
import random

from Heart import Heart
from Score import Score
from Wallpaper import Wallpaper

pygame.init()

window_width = 1465
window_height = 800
scoreboard_height = 100
window = pygame.display.set_mode((window_width, window_height))
wallapper = Wallpaper(window_width, window_height)
timer_event = pygame.USEREVENT + 1

# Score
score = 0
text = Score(str(score))

pygame.time.set_timer(timer_event, 1000)

# Instances
hearts = []
for _ in range(0, 10):
  hearts.append(Heart(random.randint(0, window_width - 50), 0))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      for heart in hearts:
        if heart.rect != '' and heart.rect.collidepoint(event.pos):
          score += 1
          hearts.remove(heart)
          text.update_score(str(score))
    elif event.type == timer_event:
      hearts.append(Heart(random.randint(0, window_width - 50), 0))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
      running = False

  # Background
  window.fill((0, 0, 0))
  wallapper.draw(window)

  # Scoreboard
  pygame.draw.rect(
    window, 
    (0, 0, 0), 
    pygame.Rect(0, window_height - scoreboard_height , window_width, scoreboard_height )
  )

  # Drawing
  for heart in hearts:
    heart.draw(window)
    heart.move()
    if heart.position_y > window_height - scoreboard_height - 50:
      hearts.remove(heart)
      score -= 5
      text.update_score(str(score))

  # Text
  window.blit(text.render_font(), (10, (window_height - scoreboard_height) + 15))
    
  pygame.display.flip()
  pygame.time.Clock().tick(120)
pygame.quit()
