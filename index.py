import pygame
import random

# Inicializar Pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Evita los Meteoritos")

# Fuente
font = pygame.font.Font(None, 74)

# Clase para la nave
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([30, 20])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0] - self.rect.width // 2
        self.rect.y = pos[1] - self.rect.height // 2

# Clase para los meteoritos
class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(SCREEN_WIDTH)
        self.rect.y = random.randrange(-20, -1)
        self.speedy = random.randrange(1, 10)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.x = random.randrange(SCREEN_WIDTH)
            self.rect.y = random.randrange(-20, -1)
            self.speedy = random.randrange(1, 10)

# Lista de todos los sprites
all_sprites = pygame.sprite.Group()
meteors = pygame.sprite.Group()

# Crear jugador
player = Player()
all_sprites.add(player)

# Crear meteoritos
for i in range(50):
    meteor = Meteor()
    all_sprites.add(meteor)
    meteors.add(meteor)

# Función para mostrar texto en pantalla
def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

# Menú inicial
def show_menu():
    screen.fill(BLACK)
    draw_text(screen, "Evita los Meteoritos", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)
    draw_text(screen, "Presiona cualquier tecla para comenzar", 22, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.flip()
    wait_for_key()

# Esperar a que se presione una tecla
def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYUP:
                waiting = False

# Bucle principal del juego
def game_loop():
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar sprites
        all_sprites.update()

        # Verificar colisiones
        if pygame.sprite.spritecollideany(player, meteors):
            running = False

        # Dibujar y actualizar pantalla
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()

        # Limitar a 60 FPS
        clock.tick(60)

    pygame.quit()

# Mostrar menú y luego iniciar el juego
show_menu()
game_loop()







