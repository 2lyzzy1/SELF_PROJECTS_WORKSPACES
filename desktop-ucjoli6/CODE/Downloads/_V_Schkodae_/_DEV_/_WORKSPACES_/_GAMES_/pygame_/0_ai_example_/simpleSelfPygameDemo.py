#import pygame as pg

#pg.init()
#

#screen = pg.display.set_mode((640, 480))


#
#pg.quit()

##################################################

import pygame

# --- 1. Initialisation ---
pygame.init()

# Paramètres de l'écran
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mouvement Simple Pygame")

# Couleurs
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
NOIR = (0, 0, 0)

# Paramètres du joueur (le carré rouge)
player_size = 50
player_x = WIDTH // 2 - player_size // 2  # Centre horizontalement
player_y = HEIGHT // 2 - player_size // 2 # Centre verticalement
player_vel = 5 # Vitesse de déplacement (en pixels par frame)

# Horloge pour contrôler la vitesse du jeu
clock = pygame.time.Clock()
FPS = 60 # Taux de rafraîchissement cible

# --- 2. Boucle de Jeu Principale ---
time0 = pygame.time.get_ticks()
i = 0
running = True
switched_ = True
while running:
    # -----------------------------
    # A. GESTION DES ÉVÉNEMENTS
    # -----------------------------
    for event in pygame.event.get():
        # L'utilisateur a cliqué sur le bouton de fermeture
        if event.type == pygame.QUIT:
            running = False

    # -----------------------------
    # B. MISE À JOUR DE L'ÉTAT (Mouvement)
    # -----------------------------
    # Récupérer l'état de toutes les touches enfoncées
    keys = pygame.key.get_pressed()
    
    # Mettre à jour la position du joueur en fonction des touches
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_vel
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_vel
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_vel

    # -----------------------------
    # C. DESSIN / RENDU
    # -----------------------------
    # Remplir l'écran de noir (effacer la frame précédente)
    SCREEN.fill(NOIR)
    
    # To Change Objects
    if keys[pygame.K_s]:
        switched_ = not( switched_ )
    
    # Dessiner le carré (Surface, Couleur, Rectangle(x, y, largeur, hauteur))
    if switched_:
        pygame.draw.rect(SCREEN, ROUGE, (player_x, player_y, player_size, player_size))

    # -----------------------------
    timeI = pygame.time.get_ticks()
    time = timeI - time0
    #
    if not (time % 5 == 5):
        if not(switched_):
            i += 1
            pygame.draw.rect(SCREEN, (200+i, 150+i, 100+i), (player_x+30, player_y+45, player_size, player_size))
            if i == 54:
                i = 0
    # _____________________________
    
    # Mettre à jour l'affichage
    pygame.display.flip()

    # Limiter le jeu à 60 images par seconde (FPS)
    clock.tick(FPS)

# --- 3. Fermeture ---
pygame.quit()
