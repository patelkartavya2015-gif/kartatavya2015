import sys as s
import pygame as p
p.init()
screen = p.display.set_mode((800, 500))
screen.fill((58, 58, 58))
p.display.set_caption("My Pygame Window")

font = p.font.SysFont("Arial", 90)
text_surface = font.render("Hello, Pygame!", True, (255, 255, 255))
rect = p.Rect(50, 200, 400, text_surface.get_height())

running = True
while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
    
    screen.blit(text_surface, rect)
    p.display.flip()