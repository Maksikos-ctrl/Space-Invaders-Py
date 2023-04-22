import pygame
import random
from constants import  bg, bg_menu, WIDTH, HEIGHT, WINDOW
from game import Player,  Enemy, collide
# import socket
# import pickle
# import os
# import time
pygame.font.init()


# SERVER_IP = "127.0.0.1"
# PORT = 1234
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((SERVER_IP, PORT))


def main():
    running = 1
    FPS = 60
    level = 0
    lives = 5
    enemy_vel = 3
    main_font = pygame.font.SysFont("comicsans", 40)
    lost_font = pygame.font.SysFont("comicsans", 60)
    player_vel = 8
    laser_vel = 8
    enemies = []
    wave_length = 5
    player = Player(300, 650)

    clock = pygame.time.Clock()

    lost = 0
    lost_count = 0 

    def redraw_window():
        WINDOW.blit(bg, (0, 0))
        # draw text
        lives_label = main_font.render(f"Pocet Zivotov: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Uroven: {level}", 1, (255, 255, 255))

        WINDOW.blit(lives_label, (10, 10))
        WINDOW.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))


        player.draw(WINDOW)

        for enemy in enemies:
            enemy.draw(WINDOW)

        player.draw(WINDOW)  

        if lost:
            lost_label = lost_font.render(f"Prehral si", 1, (255, 255, 255))
            WINDOW.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))



        
        pygame.display.update()

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                start_menu()
                
      

        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = 1
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
               
                running = 0
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(enemy)
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = 0

        keys = pygame.key.get_pressed()   
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and player.x - player_vel > 0:
            player.x -= 5

        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and player.x + player_vel + player.get_width() < WIDTH:
            player.x += 5

        if (keys[pygame.K_w] or keys[pygame.K_UP]) and player.y - player_vel > 0:
            player.y -= 5

        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and player.y + player_vel + player.get_height() + 15 < HEIGHT:
            player.y += 5

        if (keys[pygame.K_SPACE]):
            player.shoot(player_vel)



      


        for enemy in enemies[:]:
            enemy.move(enemy_vel)   
            enemy.move_lasers(laser_vel, player)

            
            if random.randrange(0, 2*FPS) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 5
                enemies.remove(enemy)    


            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)


def start_menu():
    running = 1
    
    title_font = pygame.font.SysFont("comicsans", 70)
    while running:
        WINDOW.blit(bg_menu, (0, 0))
        title_label = title_font.render("Klikni pre zacatie", 1, (255, 255, 255))
        play_button = pygame.image.load("assets/play_button.png")
        play_button = pygame.transform.scale(play_button, (play_button.get_width() // 2, play_button.get_height() // 2))
        
        play_button = pygame.transform.scale(play_button, (140, 80))
        
        
        WINDOW.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))

       
        WINDOW.blit(play_button, (300, 650))
        
        

        
        pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    main()

    pygame.quit()                
                
                 
start_menu()

main()    


































    










