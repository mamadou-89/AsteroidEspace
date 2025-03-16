import pygame

class Projectil(pygame.sprite.Sprite):
    def __init__(self,projectil_event):
        super().__init__()
        self.attack=10
        self.velocity=5
        self.projectil_event=projectil_event
        self.projectil_color=(0,128,255)
        self.projectil_pos=(self.projectil_event.game.player.rect.x + 30,self.projectil_event.game.player.rect.y -5)
        self.rect=pygame.draw.circle (self.projectil_event.game.screen,self.projectil_color,self.projectil_pos,10)
        #self.image=pygame.image.load()
        #self.image=pygame.transform.scale(self.image,(10,10))
        #self.rect=self.image.get_rect()
        #self.rect.x=self.projectil_event.game.player.rect.x + 25
        #self.rect.y=self.projectil_event.game.player.rect.y + 25
    
    def moving(self):
        self.rect.y-=self.velocity


    def draw(self,screen):
        pygame.draw.circle (self.projectil_event.game.screen,self.projectil_color,(self.rect.x,self.rect.y),10)

    def collideDetection(self):
        if self.rect.y <=0:
            self.projectil_event.removeProjectil(self)
        for meteor in self.projectil_event.game.meteor_event.meteors_group :
            if pygame.sprite.collide_rect(self,meteor):
                meteor.damage(self.attack)
                self.projectil_event.removeProjectil(self)


