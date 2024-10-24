import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.button_pressed = False

    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation) 
        self.position += forward * PLAYER_SPEED * dt
    
    def bulletspawn(self, radius, position, velocity):
        shot = Shot(position.x, position.y, radius)
        shot.velocity = velocity

    def shoot(self):
        position = self.position
        velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
        self.bulletspawn(SHOT_RADIUS, position, velocity)

    def update(self, dt):
        self.timer -= dt
        if self.timer > 0:
            self.button_pressed = False
        else:
            self.button_pressed = True
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            if self.button_pressed:
                self.shoot()

    


