
import pygame
import socket
from constants import RED_player, GREEN_player, BLUE_player, player, RED_LASER, GREEN_LASER, BLUE_LASER, YELLOW_LASER, HEIGHT


class Ship:
    COOLDOWN = 30
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.player_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        

    def draw(self, window):
        window.blit(self.player_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def get_width(self):
        return self.player_img.get_width()
    
    def get_height(self):
        return self.player_img.get_height()
    
    def shoot(self, vel):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def cool_down(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def move_lasers(self, vel, obj):
        self.cool_down()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser) 
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)


    # def to_dict(self):
    #     return {"x": self.x, "y": self.y, "health": self.health, "lasers": self.lasers}

    # @staticmethod
    # def from_dict(data):
    #     ship = Ship(data["x"], data["y"], data["health"])
    #     ship.lasers = data["lasers"]
    #     return ship            




class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.player_img = player
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.player_img)
        self.max_health = health


    def move_lasers(self, vel, objs):
        self.cool_down()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser) 
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                            

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.player_img.get_height() + 10, self.player_img.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.player_img.get_height() + 10, self.player_img.get_width() * (self.health/self.max_health), 10))







    


class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_player, RED_LASER),
        "green": (GREEN_player, GREEN_LASER),
        "blue": (BLUE_player, BLUE_LASER)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.player_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.player_img)


    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


class Laser(Ship):
    def __init__(self, x, y, img):
        super().__init__(x, y, health=100)
        self.laser_img = img
        self.mask = pygame.mask.from_surface(self.laser_img)

    def draw(self, window):
        window.blit(self.laser_img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)    


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None
