import pygame
from Projectil import Projectil

class Projectil_event():
    def __init__(self,game):
        self.game=game
        self.projectils_group=[]

    def addProjectil(self):
        self.projectils_group.append( Projectil(self) )

    def removeProjectil(self,projectil):
        if (projectil in self.projectils_group):
            self.projectils_group.remove(projectil)

    def removeAllProjectil(self):
        for projectil in self.projectils_group:
            if (projectil in self.projectils_group):
                self.projectils_group.remove(projectil)

    def updateProjectils(self):
        for projectil in self.projectils_group:
            projectil.draw(self.game.screen)
