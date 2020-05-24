import pygame
import random

class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        pygame.font.init()
        self.game = game
        self.health = 1
        self.max_health = 1
        self.attack = 0.3
        self.velocity = random.randint(1,2)
        self.image = pygame.image.load('assets/spacemonster.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,600)
        self.rect.y = -50
        self.death_count = 0

    def update_health_bar(self, surface):
        #Definir une couleur pour la jauge de vie
        if self.health <= (self.max_health / 3):
            bar_color = (177, 9, 0)
        elif self.health <= (self.max_health / 2):
            bar_color = (207, 70, 0)
        else:
            bar_color = (111,210,46)

    def damage(self, amount):
        #infliger les degats
        self.health-= amount

        #Quand le monstre subit des degats on verifie ses HP
        if self.health <=0:
            self.death_count+=1
            #Reapparaitre comme un nouveau monstre
            if self.death_count > 10:
                self.rect.x = random.randint(0, 600)
                self.rect.y = -50
                self.velocity = random.randint(1, 2)
                self.health = self.max_health + random.randint(0,3)
            elif self.death_count > 5:
                self.rect.x = random.randint(0, 600)
                self.rect.y = -50
                self.velocity = random.randint(1, 2)
                self.health = self.max_health + random.randint(0,2)
            else:
                self.rect.x = random.randint(0, 600)
                self.rect.y = -50
                self.velocity = random.randint(1,2)
                self.health = self.max_health


    def forward(self):
        if not self.game.check_collision(self, self.game.all_players) or self.rect.y >= 800:
            if self.rect.y >= 800:
                if self.death_count > 10:
                    self.rect.x = random.randint(0, 600)
                    self.rect.y = -50
                    self.velocity = random.randint(1, 2)
                    self.health = self.max_health + random.randint(0, 3)
                elif self.death_count > 5:
                    self.rect.x = random.randint(0, 600)
                    self.rect.y = -50
                    self.velocity = random.randint(1, 2)
                    self.health = self.max_health + random.randint(0, 2)
                else:
                    self.rect.x = random.randint(0, 600)
                    self.rect.y = -50
                    self.velocity = random.randint(1, 2)
                    self.health = self.max_health
            else:
                self.rect.y += self.velocity
        #si le monstre est en collision avec le joueur
        else:
            #infliger des degats au joueur
            self.game.player.damage(self.attack)