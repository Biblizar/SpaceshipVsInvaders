import pygame

#Definir la classe qui va gerer le projectile du joueur
class Projectile(pygame.sprite.Sprite):

    #Definir le constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 6
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x
        self.rect.y = player.rect.y
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        #faire tourner le projectile
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.y -= self.velocity
        self.rotate()

        #verifier si le projectile rentre en collision avec le monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            #infliger des degats
            monster.damage(self.player.attack)

        #condition pour vertifier si le projectile n'est plus sur l'écran
        if self.rect.x > 1080:
            #suppression du projectile
            self.remove()
