import pygame
import random
import os

# Simple demo: 1 player sprite, 7 enemy sprites. When an enemy collides with the player, the enemy is removed.
# Requires: pip install pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
RED = (200, 40, 40)
BLUE = (40, 120, 200)

def load_image(name, size=None):
    """Load an image from the script directory. Return Surface or None on failure."""
    path = os.path.join(os.path.dirname(__file__), name)
    try:
        img = pygame.image.load(path).convert_alpha()
        if size:
            img = pygame.transform.smoothscale(img, size)
        return img
    except Exception:
        return None

# Scoring configuration
POINTS_PER_KILL = 1  # base points awarded per enemy
USE_ROUND_MULTIPLIER = False  # if True, awarded points = POINTS_PER_KILL * round_num

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        img = load_image("player.png", (50, 50))
        if img:
            self.image = img
        else:
            self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.rect(self.image, BLUE, (0, 0, 50, 50))
        self.rect = self.image.get_rect(center=pos)
        self.speed = 6

    def update(self, keys_pressed):
        dx = (keys_pressed[pygame.K_RIGHT] - keys_pressed[pygame.K_LEFT]) * self.speed
        dy = (keys_pressed[pygame.K_DOWN] - keys_pressed[pygame.K_UP]) * self.speed
        self.rect.x += dx
        self.rect.y += dy
        # Keep inside screen
        self.rect.clamp_ip(pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        img = load_image("enemy.png", (40, 40))
        if img:
            self.image = img
        else:
            self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.circle(self.image, RED, (20, 20), 20)
        self.rect = self.image.get_rect(center=pos)
        self.vx = random.choice([-3, -2, -1, 1, 2, 3])
        self.vy = random.choice([-3, -2, -1, 1, 2, 3])

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        # bounce on screen edges
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > SCREEN_HEIGHT:
            self.vy = -self.vy


def spawn_enemies(count, enemies, all_sprites, round_num):
    """Spawn `count` enemies and scale their speed by round number."""
    for _ in range(count):
        pos = (random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50))
        e = Enemy(pos)
        factor = 1 + (round_num - 1) * 0.1
        e.vx *= factor
        e.vy *= factor
        enemies.add(e)
        all_sprites.add(e)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Collision Demo: Kill enemy on contact")
    clock = pygame.time.Clock()

    # Sprite groups
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # Create player in center
    player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    all_sprites.add(player)

    # Rounds setup
    round_num = 1
    start_enemy_count = 7
    enemy_count = start_enemy_count
    score = 0

    spawn_enemies(enemy_count, enemies, all_sprites, round_num)

    running = True
    font = pygame.font.SysFont(None, 36)

    # Load background (scaled to screen) if available
    bg = load_image("background.png", (SCREEN_WIDTH, SCREEN_HEIGHT))

    while running:
        dt = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)
        enemies.update()

        # Collision detection: if enemy collides with player -> remove (kill) that enemy
        collided = pygame.sprite.spritecollide(player, enemies, dokill=True)
        # dokill=True will call kill() on each enemy collided, removing it from groups
        if collided:
            multiplier = round_num if USE_ROUND_MULTIPLIER else 1
            points = POINTS_PER_KILL * multiplier
            score += len(collided) * points

        # Draw background and sprites
        if bg:
            screen.blit(bg, (0, 0))
        else:
            screen.fill(WHITE)
        all_sprites.draw(screen)

        # Show remaining enemies, round, score, and points-per-kill
        text = font.render(f"Enemies left: {len(enemies)}", True, (0, 0, 0))
        screen.blit(text, (10, 10))

        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 40))

        ppk_text = font.render(f"Points/kill: {POINTS_PER_KILL}{' x round' if USE_ROUND_MULTIPLIER else ''}", True, (0, 0, 0))
        screen.blit(ppk_text, (10, 70))

        round_text = font.render(f"Round: {round_num}", True, (0, 0, 0))
        screen.blit(round_text, (SCREEN_WIDTH - 120, 10))

        if len(enemies) == 0:
            # Short inter-round pause with message, then start next round (increase difficulty)
            msg = font.render(f"Round {round_num} cleared! Next round starting...", True, (0, 150, 0))
            screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            # wait while still processing quit events
            wait_time = 1000  # ms
            start_wait = pygame.time.get_ticks()
            while pygame.time.get_ticks() - start_wait < wait_time:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                pygame.time.delay(50)
            if not running:
                break
            # prepare next round
            round_num += 1
            enemy_count = min(start_enemy_count + (round_num - 1), 30)  # cap enemies at 30
            spawn_enemies(enemy_count, enemies, all_sprites, round_num)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
