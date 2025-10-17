import pygame
import math
from  game import Game
pygame.init()


# generer la fenetre de notre jeu
pygame.display.set_caption("comet fall Game")
screen = pygame.display.set_mode((1080, 720))

#importer de charger l'arriere plan de notre jeu
background = pygame.image.load('PygameAssets-main/bg.jpg')

#importer chargher notre baniiere
banner = pygame.image.load('PygameAssets-main/banner.png')
banner = pygame.transform.scale(banner,(500,500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

#import charger notre button pour lancer la partie
play_button = pygame.image.load('PygameAssets-main/button.png')
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)


#charger notre jeu
game = Game()

running = True

#boucle tant aue cette condition est vrai
while running:
    #appliquer l'arriere plan de notre jeu
    screen.blit(background, (0, -200))

    #verifier si notre jeu a commence ou non
    if game.is_playing:
        #declancher les instruction de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commence
    else:
        #ajouter mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner,banner_rect)

    #mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme cette fenetre
    for event in pygame.event.get():
        #que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")
        #detecter si un joeur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecter si la touche espace est enclenchee
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verifier pour savoir si la souris est en collision avec le button de jeu
            if play_button_rect.collidepoint(event.pos):
                #metre le jeu en mode lancer
                game.start()