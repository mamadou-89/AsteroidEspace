import pygame
from math import ceil

class SpaceShip (pygame.sprite.Sprite):
    def __init__(self,type,game):
        super().__init__()
        self.image=pygame.image.load("./assets/players/spaceShip"+str(type)+".png")
        self.image= pygame.transform.scale(self.image,(50,50))
        self.game=game
        self.max_health=100
        self.health = self.max_health
        self.attack=10
        self.velocity=10
        self.rect=self.image.get_rect()
        self.rect.x = ceil(game.screen.get_width()/2 )
        self.rect.y =ceil(game.screen.get_height()-50) 


    def updateHealthBar(self):
        bar_color1=(0,0,0)
        bar_color2=(51,255,51)
        bar_pos1=[self.rect.x-20,self.rect.y-10,self.max_health,5]
        bar_pos2=[self.rect.x-20,self.rect.y-10,self.health,5]
        pygame.draw.rect(self.game.screen,bar_color1,bar_pos1)
        pygame.draw.rect(self.game.screen,bar_color2,bar_pos2)




    def reset(self):
        self.health =self.max_health
        self.rect.x = ceil(self.game.screen.get_width()/2 )
        self.rect.y =ceil(self.game.screen.get_height()-50) 



    def damage(self,damage):
        self.health-=damage
        if self.health <=0 :
            self.game.game_over=True

    def left(self):
        self.rect.x-=self.velocity
    def right(self):
        self.rect.x+=self.velocity
    def up(self):
        self.rect.y-=self.velocity
    def down(self):
        self.rect.y+=self.velocity

        
