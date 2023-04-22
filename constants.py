import pygame
import os

WIDTH, HEIGHT = 850, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")


RED_player = pygame.image.load(os.path.join("assets", "spaceShips_002.png"))
GREEN_player = pygame.image.load(os.path.join("assets", "spaceShips_003.png"))
BLUE_player = pygame.image.load(os.path.join("assets", "spaceShips_004.png"))

RED_player = pygame.transform.scale(RED_player, (RED_player.get_width() // 3, RED_player.get_height() // 3))
GREEN_player = pygame.transform.scale(GREEN_player, (GREEN_player.get_width() // 3, GREEN_player.get_height() // 3))
BLUE_player = pygame.transform.scale(BLUE_player, (BLUE_player.get_width() // 3, BLUE_player.get_height() // 3))

player = pygame.image.load(os.path.join("assets", "ship.png"))
player = pygame.transform.scale(player, (player.get_width() // 2, player.get_height() // 2))

RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "space.png")), (WIDTH, HEIGHT))
bg_menu = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg_menu.jpg")), (WIDTH, HEIGHT))