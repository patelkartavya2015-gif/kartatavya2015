import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen.fill((58, 58, 58))
pygame.display.set_caption("My Pygame Window")

# Load the image ONCE, before the loop
try:
    grass_surface = pygame.image.load("grass.png")
    grass_surface = pygame.transform.scale(grass_surface, (300, 300))
except pygame.error as e:
    print(f"Error loading image: {e}")
    # Handle the error, perhaps exit the game or use a placeholder
    running = False 
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Draw (blit) the image to the screen inside the loop
    # The second argument (0, 0) specifies the top-left position
    if 'grass_surface' in locals(): # Only blit if successfully loaded
        screen.blit(grass_surface, (100, 100))

    # Update the display to show the newly blitted image
    pygame.display.flip()

pygame.quit()
