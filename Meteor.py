import pygame
from random import randint

class Meteor (pygame.sprite.Sprite):
    def __init__(self,meteor_event):
        super().__init__()
        self.type=randint(0,1) # deux types de méteors
        self.origin_image=pygame.image.load("./assets/asteroides/asteroid"+str(self.type)+".png")
        self.origin_image= pygame.transform.scale(self.origin_image,(50,50))
        self.image=self.origin_image
        self.meteor_event=meteor_event
        self.velocity= randint(1,3)
        self.rect=self.image.get_rect()
        self.rect.x = randint(0,meteor_event.game.screen.get_width()-self.image.get_width () )
        self.rect.y -=  randint(0,meteor_event.game.screen.get_height())
        self.angle=0
        if self.type == 1:
            self.attack=10
            self.maxHealth=50
        else:
            self.attack=25
            self.maxHealth=75
        self.health = self.maxHealth
       

    def rotate(self):
        self.angle+=8
        self.image=pygame.transform.rotozoom(self.origin_image,self.angle)
        

    def falling (self):
        self.rect.y+=self.velocity

        
    def collideDetection(self):
        if self.rect.y >= self.meteor_event.game.screen.get_height():
            self.meteor_event.removeMeteor(self)
        elif pygame.sprite.collide_rect(self,self.meteor_event.game.player):
            self.meteor_event.game.player.damage(self.attack)
            self.meteor_event.removeMeteor(self)
    
    
    def damage(self,attack):
        self.health-=attack
        if self.health<=0:
            self.meteor_event.removeMeteor(self)
            self.meteor_event.game.score+=1
