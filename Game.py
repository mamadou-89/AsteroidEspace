import pygame
from Player import SpaceShip
from Meteor_event import Meteor_event
from Projectil_event import Projectil_event
from math import ceil 


class Game():
    def __init__(self):
        pygame.init()
        self.isRunning=None
        pygame.display.set_caption("AsteroïdEscape")
        pygame.display.set_icon(pygame.image.load("./assets/icons/meteor.png"))
        self.screen = pygame.display.set_mode((800,500))
        self.background=pygame.image.load("./assets/background/galaxy.jpg")
        self.background = pygame.transform.scale(self.background,(800,500))
        self.play_button=pygame.image.load("./assets/icons/start-button.png")
        self.play_button= pygame.transform.scale(self.play_button,(150,150))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x=ceil(self.screen.get_width()/2)-70 #utiliser les coordonnées du rectangle play_button
        self.play_button_rect.y=ceil(self.screen.get_height()/2)-70 #utiliser les coordonnées du rectangle play_button
        self.clock= pygame.time.Clock()
        self.player= SpaceShip(1,self)
        self.moves={}
        self.meteor_event= Meteor_event (self)
        self.projectil_event= Projectil_event(self)
        self.game_over=None
        self.score =None

    def launch(self):
        self.isRunning=False
        self.game_over=False
        self.screen.blit(self.background,self.screen.get_rect())
        self.screen.blit(self.play_button,self.play_button_rect)
        self.score=0
        pygame.display.flip()


    def start(self):
        self.isRunning=True
        self.refresh()
    
    def buttonPressed(self): #Actions spécifique à faire si un bouton est présser
        if self.moves.get(pygame.K_LEFT) and self.player.rect.x >0:
            self.player.left()
            if self.moves.get(pygame.K_UP) and self.player.rect.y >0 :
                self.player.up()
            elif self.moves.get(pygame.K_DOWN) and self.player.rect.y < self.screen.get_height() - self.player.rect.height :
                self.player.down()

        if self.moves.get(pygame.K_RIGHT) and self.player.rect.x < self.screen.get_width() - self.player.rect.width: 
            self.player.right()
            if self.moves.get(pygame.K_UP) and self.player.rect.y >0 :
                self.player.up()
            elif self.moves.get(pygame.K_DOWN) and self.player.rect.y < self.screen.get_height() - self.player.rect.height :
                self.player.down()

        if self.moves.get(pygame.K_DOWN) and self.player.rect.y < self.screen.get_height() - self.player.rect.height:
            self.player.down()
            if self.moves.get(pygame.K_RIGHT) and self.player.rect.x < self.screen.get_width()-self.player.rect.width:
                self.player.right()
            elif self.moves.get(pygame.K_LEFT) and self.player.rect.x >0:
                self.player.left()

        if self.moves.get(pygame.K_UP) and self.player.rect.y >0 :
            self.player.up()
            if self.moves.get(pygame.K_RIGHT) and self.player.rect.x < self.screen.get_width()-self.player.rect.width:
                self.player.right()
            elif self.moves.get(pygame.K_LEFT) and self.player.rect.x >0 :
                self.player.left()

    def eventChecking(self):
        res=True
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                res=False
            elif self.isRunning:  
                if event.type == pygame.KEYDOWN: #appuis sur une direction
                        if event.key==pygame.K_SPACE:
                            self.projectil_event.addProjectil()

                        else:
                            self.moves[event.key]=True
                    
                elif event.type == pygame.KEYUP: #relachement d'une direction 
                        self.moves[event.key]=False
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:#appuis sur le boutton de la souris
                    if self.play_button_rect.collidepoint(event.pos):
                        self.start()
        
        return res

    def movingEntity(self): # gère le mouvementdes différentes entités
        for meteor in self.meteor_event.meteors_group:
            meteor.falling()
            meteor.collideDetection()
        for projectil in self.projectil_event.projectils_group:
            projectil.moving()
            projectil.collideDetection()

    
    def checkGameOver(self):
        if self.game_over:
            self.meteor_event.removeAllMeteors()
            self.projectil_event.removeAllProjectil()
            self.player.reset()
            self.launch()

    def refresh (self): # rafraichis les images sur l'écrans 
        self.screen.blit(self.background,self.background.get_rect())
        self.screen.blit(self.player.image,self.player.rect)
        self.meteor_event.meteors_group.draw(self.screen)
        self.projectil_event.updateProjectils()
        self.player.updateHealthBar()

        #autre choses à venir
        pygame.display.flip()
        
    def loop(self):
        self.meteor_event.loop()
        self.movingEntity()
        self.buttonPressed()
        self.refresh()
        self.checkGameOver()


    def exit(self):
        pygame.quit()
        exit(0)
    


