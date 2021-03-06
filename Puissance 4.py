import numpy as np
import time


# Génère la grille de jeu
plateau = []
plateau.append(["/"," " ,"A","B","C","D","E","F","G"])
for i in range(6):
    plateau.append([i+1,"|",".",".",".",".",".",".","."])


# Affiche une matrice d'une manière 'propre' : servira à afficher la grille de jeu
def Affiche(M):
    nligne=len(M)
    ncolonne=len(M[0])
    for i in range(0,nligne):
        for j in range(0,ncolonne) :
            print(M[i][j],end=' ')
        print()


# Tour du joueur :
#Teste si la lettre entrée par le joueur est dans la liste ref, et si c'est le cas renvoie 0 pour A, 1 pour B, ect

def joueur(reponse) :
    #reponse = input("Où voulez-vous jouer ? ")
    ref = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    if reponse in ref :
        return ref.index(reponse)
    else:
        print('Error')
        joueur()
# Rappel de la fonction si erreur :
# print('Veuillez entrer la lettre correspondant la colonne choisie')
# joueur()
# ?


#Place le pion du joueur dans la première case innocupé de la colonne numérotée 'nbre'
def plaçagedupion(nbre):
    n = 1
    for k in range(5):
        if plateau[nbre+1][k+2] == '.':
            n += 1
    plateau[n][nbre+2] = "x"
# Pour l'animation : il faudrait modifier 'en direct' le plateau qui serait tout le temps affiché


Affiche(plateau)
#plaçagedupion(joueur())
ref = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for l in ref :
    print(l)
    plaçagedupion(joueur(l))
Affiche(plateau)

