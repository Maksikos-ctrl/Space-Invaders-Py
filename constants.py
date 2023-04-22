import pygame
import os

WIDTH, HEIGHT = 850, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")


RED_player = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_player = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_player = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

player = pygame.image.load(os.path.join("assets", "ship.png"))
player = pygame.transform.scale(player, (player.get_width() // 2, player.get_height() // 2))

RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "space.png")), (WIDTH, HEIGHT))
bg_menu = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_menu.jpg")), (WIDTH, HEIGHT))