from Game import *

if __name__=="__main__" :

    game=Game()

    game.launch()

    running=True

    #boucle principal du jeu

    while running:
        game.clock.tick(60)
        if game.isRunning:
            game.loop()
        running= game.eventChecking()


    game.exit()

        
