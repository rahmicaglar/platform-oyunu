import pygame
import sys
import random

# Pygame'i başlat
pygame.init()

# Ekran boyutları
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Quest")

# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FPS (saniye başına kare)
FPS = 60
clock = pygame.time.Clock()

# Seviye
level = 1

def draw_level():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Seviye: {level}", True, BLACK)
    screen.blit(text, (10, 10))

def show_start_screen():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 74)
    title_text = font.render("Platformer Quest", True, BLACK)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))
    
    font = pygame.font.Font(None, 36)
    
    start_text = font.render("Oyuna Başla", True, BLACK)
    
    start_rect = start_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    screen.blit(start_text, start_rect.topleft)
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    waiting = False  # Oyuna başla

def show_game_over_screen():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 74)
    game_over_text = font.render("Oyun Bitti", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 4))
    
    font = pygame.font.Font(None, 36)
    
    restart_text = font.render("Yeniden Başlamak İçin Bir Tuşa Basın", True, BLACK)
    restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(restart_text, restart_rect.topleft)
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:  # Herhangi bir tuşa basıldığında
                waiting = False  # Oyunu yeniden başlat

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 100)
        self.speed_x = 0
        self.speed_y = 0
        self.gravity = 0.8
        self.jump_count = 0  # Zıplama sayısını takip eden sayaç

    def apply_gravity(self):
        self.speed_y += self.gravity
        self.rect.y += self.speed_y

    def jump(self):
        if self.jump_count < 2:  # Eğer 2 kez zıplamadıysa
            self.speed_y = -15  # Zıplama hızı
            self.jump_count += 1  # Zıplama sayısını artır

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -5
        if keys[pygame.K_RIGHT]:
            self.speed_x = 5
        if keys[pygame.K_SPACE]:
            self.jump()

        self.rect.x += self.speed_x
        self.apply_gravity()

        # Platformlarla çarpışma kontrolü
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            if self.speed_y > 0:  # Eğer aşağı doğru hareket ediyorsa
                self.rect.bottom = hits[0].rect.top  # Karakteri platformun üzerine yerleştir
                self.speed_y = 0  # Hızı sıfırla
                self.jump_count = 0  # Zıplama sayısını sıfırla

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, speed_x, speed_y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.speed_x = -self.speed_x

        if self.rect.bottom >= HEIGHT or self.rect.top <= 0:
            self.speed_y = -self.speed_y

class Teleport(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

def create_random_level():
    global platforms, enemies, teleport, previous_platform_x, previous_platform_y

    platforms.empty()
    enemies.empty()

    # Alt taban (yer) platformunu ekleyelim
    ground = Platform(0, HEIGHT - 40, WIDTH, 40)
    platforms.add(ground)
    all_sprites.add(ground)

    # İlk platformu oyuncunun zıplama mesafesine göre yerleştirelim
    initial_platform_y = HEIGHT - 150  # Oyuncunun rahatça zıplayabileceği bir mesafe
    initial_platform_x = WIDTH // 2 - 100  # Oyuncunun başlangıç pozisyonuna yakın
    initial_platform = Platform(initial_platform_x, initial_platform_y, 200, 20)
    platforms.add(initial_platform)
    all_sprites.add(initial_platform)

    previous_platform_y = initial_platform_y
    previous_platform_x = initial_platform_x

    num_platforms = random.randint(10, 15 + level)  # Platform sayısını artırdık

    for _ in range(num_platforms):
        # Yeni platformun x ve y pozisyonunu belirle
        max_jump_horizontal = 250  # Yatayda maksimum zıplama mesafesi
        max_jump_vertical = 150  # Dikeyde maksimum zıplama mesafesi

        min_x = max(0, previous_platform_x - max_jump_horizontal)
        max_x = min(WIDTH - 200, previous_platform_x + max_jump_horizontal)
        x = random.randint(min_x, max_x)

        min_y = previous_platform_y - max_jump_vertical
        max_y = previous_platform_y - 50  # Minimum mesafe (50 piksel) bırakıyoruz
        y = random.randint(min_y, max_y)

        # Platformların üst üste binmesini önlemek için mesafeleri kontrol et
        if previous_platform_y - y > 50:  # Önceki platformla yeni platform arasında yeterli mesafe olmalı
            platform = Platform(x, y, 200, 20)
            platforms.add(platform)
            all_sprites.add(platform)

            previous_platform_y = y  # Yeni platformun y pozisyonunu kaydet
            previous_platform_x = x  # Yeni platformun x pozisyonunu kaydet

    # Işınlanma noktasını son platformdan biraz yukarıya ekleyelim
    teleport = Teleport(previous_platform_x + 50, previous_platform_y - 100)
    all_sprites.add(teleport)

    # Rastgele toplar ekle
    num_balls = level
    for _ in range(num_balls):
        x = random.choice([0, WIDTH - 30])
        y = random.randint(50, HEIGHT - 50)
        speed_x = random.choice([3 + level, -3 - level])
        speed_y = random.choice([3 + level, -3 - level])
        ball = Ball(x, y, speed_x, speed_y)
        enemies.add(ball)
        all_sprites.add(ball)

def add_new_platform():
    global platforms, all_sprites, previous_platform_y, previous_platform_x

    # Yeni platform için bir yer belirle
    max_jump_horizontal = 250  # Yatayda maksimum zıplama mesafesi
    min_x = max(0, previous_platform_x - max_jump_horizontal)
    max_x = min(WIDTH - 200, previous_platform_x + max_jump_horizontal)
    x = random.randint(min_x, max_x)
    y = previous_platform_y - 150  # Yeni platformun y pozisyonu önceki platformun biraz üstünde olsun

    platform = Platform(x, y, 200, 20)
    platforms.add(platform)
    all_sprites.add(platform)

    previous_platform_y = y  # Yeni platformun y pozisyonunu kaydet
    previous_platform_x = x  # Yeni platformun x pozisyonunu kaydet

def load_new_map():
    global level

    all_sprites.empty()
    player.rect.center = (WIDTH // 2, HEIGHT - 100)
    all_sprites.add(player)

    create_random_level()

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

load_new_map()

def game_loop():
    global teleport, level

    show_start_screen()

    scroll_y = 0  # Kayma miktarını takip eden değişken

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        all_sprites.update()

        if pygame.sprite.spritecollide(player, enemies, False):
            show_game_over_screen()  # Oyun Bitti ekranını göster
            load_new_map()  # Oyunu yeniden başlat

        # Yukarı doğru kayma efekti
        if player.rect.top <= HEIGHT // 3:  # Oyuncu ekranın üst kısmına yaklaştığında kaymaya başla
            scroll_y = 3  # Kayma miktarını küçük yap
            player.rect.top += scroll_y
            for sprite in all_sprites:
                sprite.rect.y += scroll_y

        hits = pygame.sprite.spritecollide(player, platforms, False)

        if pygame.sprite.spritecollide(player, pygame.sprite.Group(teleport), False):
            level += 1  # Seviye artır

            if level % 2 == 0:  # Her 2 seviyede bir yeni platform ekle
                add_new_platform()

            load_new_map()

        screen.fill(WHITE)
        all_sprites.draw(screen)
        draw_level()

        pygame.display.flip()
        clock.tick(FPS)

game_loop()

