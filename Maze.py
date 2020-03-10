*** Blame Battlebushost, JessieProductions, hellcat ***

import pygame
import time

pygame.init()
win = pygame.display.setmode((500, 500))
pygame.display.setcaption("PySnake")
x = 50
y = 50
width = 40
height = 60
vel = 10

run = True
while run:
 pygame.time.delay(100)
 
 for event in pygame.event.get():
  if event.type ==pygame.QUIT:
   run = False
   
   keys pygame.key.get_pressed()
   
   if keys[pygame.K_LEFT]:
      x -= vel
   if keys[pygame.K_RIGHT]:
      x += vel
   if keys[pygame.K_UP]:
      y -= vel
   if keys[pygame.K_DOWN]:
     y += vel
   if keys[pygame.K_ESCAPE}:
     pygame.display.setcaption("Your teying to say you like dos better than me, right?")
     time.delay(5)
     run = False
   win.fill((0, 0, 0))
   pygame.draw.circle(win, (255, 0, 0), (x, y, width, height))
   pygame.display.update()
pygame.quit()
