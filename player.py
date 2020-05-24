import pygame
from projectile import Projectile

#CREATION D'UNE CLASSE JOUEUR
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 1
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
        self.son = pygame.mixer.Sound("assets/sounds/tir.ogg")

    def damage(self, amount):
        if self.health - amount > amount:
            #infliger les degats
            self.health -= amount
        else:
            #si le joueur n'a plus de points de vie
            self.game.game_over()



    def update_health_bar(self, surface):
        #Definir une couleur pour la jauge de vie
        if self.health <= (self.max_health / 3):
            bar_color = (177, 9, 0)
        elif self.health <= (self.max_health / 2):
            bar_color = (207, 70, 0)
        else:
            bar_color = (111,210,46)

        #Dessiner la barre de vie
        pygame.draw.rect(surface, (60,63,60), [600,750 , self.max_health, 15])
        pygame.draw.rect(surface, bar_color, [600,750 , self.health, 15])

    def launch_projectil(self):
        #creer une nouvelle instance de projectile
        self.all_projectiles.add(Projectile(self))
        self.son.play()

    def move_right(self):
        #déplacement possible si pas de collision avec monstres
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

