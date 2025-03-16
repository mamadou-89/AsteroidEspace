import pygame
from Meteor import Meteor


class Meteor_event():
    def __init__(self,game):
        self.loading=0
        self.game=game
        self.difficulty=1 # revoir vers la fin du projet ( prendre une difficulté croissante en fonction du temps écoulé)
        self.meteors_group=pygame.sprite.Group()

    def loadEvent(self):
        #self.percent += self.difficulty /100 
        self.loading += self.difficulty 
    
    def addMeteor(self):
        self.meteors_group.add(Meteor (self) )

    def removeMeteor(self,meteor):
        self.meteors_group.remove(meteor)

    def removeAllMeteors(self):
        for meteor in self.meteors_group:
            self.meteors_group.remove(meteor)
    
    def loop(self):
        self.loadEvent()
        if self.loading==100:
            self.addMeteor()
            self.loading=0
        


