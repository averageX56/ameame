import math
from random import choice
from random import randint
import numpy as np
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    def __init__(self, screen: pygame.Surface, y=550):
        self.screen = screen
        self.x = gun.x
        self.y = y
        self.r = 20
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 0


    def move(self):
        global balls
        self.vy -= 1
        self.x += self.vx
        self.y -= self.vy
        if self.y > 575:
            self.y = 565
            self.vy = -0.9 * self.vy
        if self.y < 50:
            self.y = 65
            self.vy = -0.9 * self.vy
        self.live +=1
        if self.live > 150:
            balls.pop()
        while True:
            self.vx = 0.99 * self.vx
            break


    def draw(self):
        self.rect = pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r)

    def hittest(self, obj):
        condition = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (self.r + obj.r) ** 2)
        return condition
class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.vx = 0
        self.x = 400
        self.cd = 400
        self.cheater = 0

    def new_gun(self):
        self.x = 400

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):

        global balls
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1] - new_ball.y), (event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * np.cos(self.an)
        new_ball.vy = - self.f2_power * np.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def fire_bb(self, event):
        global bb, snaryad
        new_bb = Broneboiny(self.screen)
        self.an = math.atan2((event.pos[1] - new_bb.y), (event.pos[0] - new_bb.x))
        new_bb.vx = 7 * np.cos(self.an)
        new_bb.vy = 7 * np.sin(self.an)
        new_bb.x = self.x
        bb.append(new_bb)
        self.cd = 400
        snaryad = 1

    def targetting(self, event):
        if event:
            self.an = np.arctan((event.pos[1]-550.00001) / (event.pos[0]-self.x + 0.00001))


    def draw(self):

        surf = pygame.image.load('gun.png').convert()
        surf_1 = pygame.image.load('base.png').convert()
        surf_1 = pygame.transform.scale(surf_1, (240, 100))
        surf = pygame.transform.scale(surf, (240, 100))
        surf_1.set_colorkey((255, 255, 255))
        surf.set_colorkey((255, 255, 255))
        if self.an > 0:
            rot = pygame.transform.rotate(surf, - 180 - 360 * self.an / (2 * np.pi))
        else:
            rot = pygame.transform.rotate(surf, - 360 * self.an / (2 * np.pi))
        rot_rect = rot.get_rect(center=(self.x, 560))
        rect_surf_1 = surf_1.get_rect(center=(self.x, 560.001))
        self.screen.blit(rot, rot_rect)
        self.screen.blit(surf_1, rect_surf_1)
        
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def move(self):
        self.x += self.vx
        if self.x < -40:
            self.x = 780
            self.cheater +=1
        if self.x > 800:
            self.x = 20
            self.cheater += 1

class Target:
    def __init__(self, screen):
        self.points = 0
        self.x = 100
        self.y = 100
        self.r = 0
        self.live = 1
        self.vx = 0
        self.vy = 0
        self.an = np.random.randint(0, 360)

    def new_target(self):

        self.x = randint(20, 780)
        self.y = randint(20, 530)
        self.r = randint(10, 15)
        self.color = RED
        self.an = np.random.randint(0, 360)

    def draw(self):
        color = RED
        self.rect = pygame.draw.circle(screen, color, (self.x, self.y), self.r)

    def move(self):
        self.vx = 30 * np.sin(self.an * 2 * np.pi / 360)
        self.vy = 30 * np.cos(self.an * 2 * np.pi / 360)
        self.x += self.vx
        self.y += self.vy
        if self.x > 800:
            self.x -= 15
            self.an = np.random.randint(0, 360)
        if self.x < 20:
            self.x += 15
            self.an = np.random.randint(0, 360)
        if self.y < 50:
            self.y +=15
            self.an = np.random.randint(0, 360)
        if self.y > 200:
            self.y -= 15
            self.an = np.random.randint(0, 360)

class Target_1:
    def __init__(self, screen):
        self.points = 0
        self.live = 1
        self.screen = screen
        self.x = 0
        self.y = 0
        self.r = 0
        self.new_target()
        self.vx = 10

    def new_target(self):
        self.x = randint(20, 780)
        self.y = randint(20, 200)
        self.r = randint(30, 40)
        self.color = CYAN

    def draw(self):
        color = CYAN
        self.rect = pygame.draw.circle(screen, color, (self.x, self.y), self.r)

    def move(self):
        self.x += self.vx
        if self.x > 750:
            self.x = 40
        if self.x < 40:
            self.x = 750

class Target_2:
    def __init__(self, screen):
        self.points = 0
        self.screen = screen
        self.x = 400
        self.y = 40
        self.bn = np.arctan((self.x - gun.x) / 530)
        self.timer = 0
        self.res = 1
        self.rev = 0

    def new_target(self):
        self.x = randint(150, 700)
        self.y = 40

    def draw(self):
        global target_2_x
        target_2_x = self.x
        sprite = pygame.transform.scale(pygame.image.load('strelok.png').convert(), (240, 100))
        sprite.set_colorkey((255, 255, 255))
        rects = sprite.get_rect(center=(self.x, self.y))
        self.screen.blit(sprite, rects)

    def bombing(self):
        self.timer += 1
        if self.timer > 60:
            new_rocket = Rocket(self.screen)
            new_rocket.bn = np.arctan((target_2_x - gun.x) / 530)
            self.bn = - np.arctan((target_2_x - gun.x) / 530)
            new_rocket.vy += 11 * np.cos(self.bn)
            new_rocket.vx += - 11 * np.sin(self.bn)
            rockets.append(new_rocket)
            self.timer = 0

    def revive(self):
        self.rev += 1
class Rocket:
    def __init__(self, screen: pygame.Surface):
         global target_2_x
         self.screen = screen
         self.x = target_2_x
         self.y = 150
         self.vx = 0
         self.vy = 0
         self.bn = 0

    def move(self):
        self.x -= self.vx
        self.y += self.vy
        if self.y > 600 or self.x < 0 or self.x > 1000:
            rockets.pop()

    def draw(self):
        surf = pygame.image.load('raketa.png').convert()
        surf = pygame.transform.scale(surf, (50, 100))
        surf.set_colorkey((255, 255, 255))
        rot = pygame.transform.rotate(surf, - self.bn / (2 * np.pi) * 360)
        rot_rect = rot.get_rect(center=(self.x, self.y))
        self.screen.blit(rot, rot_rect)

    def hittest(self):
        cond = (self.x - gun.x) ** 2 + (self.y - 560) ** 2 < 9000
        return cond

class Vrag:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = 20
        self.r = 20
        self.vx = 0
        self.vy = 0
        self.an = 0
        self.y = 100
        self.omega = 0



    def draw(self):

        surf = pygame.image.load('vrag_gun.png').convert()
        surf_1 = pygame.image.load('vrag.png').convert()
        surf_1 = pygame.transform.scale(surf_1, (100, 360))
        surf = pygame.transform.scale(surf, (100, 360))
        surf_1.set_colorkey((255, 255, 255))
        surf.set_colorkey((255, 255, 255))
        rot = pygame.transform.rotate(surf,90 - 360 * self.an / (2 * np.pi))
        rot_rect = rot.get_rect(center=(20, self.y))
        rect_surf_1 = surf_1.get_rect(center=(20, self.y))
        self.screen.blit(rot, rot_rect)
        self.screen.blit(surf_1, rect_surf_1)

    def attack(self):
        new_rocket = Rocket(self.screen)
        new_rocket.bn = self.an - np.pi / 2
        new_rocket.x = 20
        new_rocket.y = self.y
        new_rocket.vx = - 10 * np.cos(self.an)
        new_rocket.vy = 10 * np.sin(self.an)
        rockets.append(new_rocket)

    def targetting(self):
        self.an += self.omega
        if self.an > 2/3 * np.pi:
            self.an = - np.pi/2
    def move(self):
        self.y += self.vy
        if self.y < 0:
            self.y = 500
        if self.y > 500:
            self.y = 0

class Broneboiny:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.x = gun.x
        self.y = 530
        self.vx = 1
        self.vy = 1
        self.bn = 0

    def move(self):
        self.x += 5 * self.vx
        self.y += 5 * self.vy
        if self.y < 0 or self.x < 0 or self.x > 1000:
            bb.pop()

    def draw(self):
        surf = pygame.image.load('bowling.png').convert()
        surf = pygame.transform.scale(surf, (50, 50))
        surf.set_colorkey((255, 255, 255))
        rot_rect = surf.get_rect(center=(self.x, self.y))
        self.screen.blit(surf, rot_rect)

    def hittest(self, obj):
        condition = (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < 9000
        return condition

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load('vietnam.png')
balls = []
bb =[]
rockets = []
counter = [0, 0]
snaryad = 1
font = pygame.font.Font('Raindrop.otf', 36)
pygame.mixer.music.load('abc.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
gun = Gun(screen)
vrag = Vrag(screen)
target = Target(screen)
target_1 = Target_1(screen)
target_2 = Target_2(screen)
brb = Broneboiny(screen)
finished = False



while not finished:
    screen.blit(bg, (0, 0))
    target.draw()
    target.move()
    target_1.draw()
    target_1.move()
    gun.move()
    vrag.move()
    target_2.draw()
    target_2.bombing()
    vrag.draw()
    gun.draw()
    vrag.targetting()
    if type(gun.cd) == int:
        gun.cd -= 2
        counter_text1 = font.render(f"{np.round(gun.cd / 100, 1)}", True, (255, 0, 0))
        if gun.cd < 0:
            gun.cd = 'Shot ready'
            counter_text1 = font.render(f"{gun.cd}", True, (255, 0, 0))
    screen.blit(counter_text1, (650, 550))
    counter_text = font.render(f"Dora {counter[0]}:{counter[1]} Abrams", True, (255, 255, 255))
    screen.blit(counter_text, (10, 550))
    for b in balls:
        b.draw()
    for r in rockets:
        r.draw()
    for p in bb:
        p.draw()
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN and snaryad < 2:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP and snaryad < 2:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEBUTTONUP and snaryad > 2:
            gun.fire_bb(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            gun.vx = -5
        elif keys[pygame.K_RIGHT]:
            gun.vx = 5
        else:
            gun.vx = 0
        if keys[pygame.K_w]:
            vrag.vy = -5
        elif keys[pygame.K_s]:
            vrag.vy = 5
        else:
            vrag.vy = 0
        if keys[pygame.K_TAB]:
            vrag.omega = 0.05
        else:
            vrag.omega = 0
        if keys[pygame.K_SPACE] and len(rockets) < 3:
            vrag.attack()
        if keys[pygame.K_2] and type(gun.cd) != int:
            snaryad += 2
    for b in balls:
        b.move()
        if b.hittest(target) or b.hittest(target_1):
            target.new_target()
            target_1.new_target()
            if len(balls) != 0:
                balls.pop()
            counter[0] += 1
    gun.power_up()
    for r in rockets:
        r.move()
        if r.hittest():
            for i in range(len(rockets)):
                rockets.pop()
            target.new_target()
            target_1.new_target()
            target_2.new_target()
            counter[1] += 1
            gun.cd = 400
            gun.new_gun()
            pygame.time.delay(10)
    for b in bb:
        b.move()
        if b.hittest(target_2):
            if len(bb) != 0:
                bb.pop()
            if len(rockets) != 0:
                rockets.pop()
            counter[0] += 2
            target_2.new_target()
    # if gun.cheater >= 16:
    #     counter[1] = 1000
pygame.quit()
