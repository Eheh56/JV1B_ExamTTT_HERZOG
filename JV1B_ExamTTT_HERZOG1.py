#1. Écrire la fonction permettant d’afficher la grille de jeu.
#Elle prend un tableau en entrée, et affiche la grille grâce aux données du tableau.

grille = ['1','2','3','4','5','6','7','8','9']


def print_grille(tableau):
    for i in range(9):
        print(tableau[i], end = ' ')
        if(i == 2 or i ==5):
            print("\n")
            print("-----------")
        elif(i != 8):
            print("|", end = ' ') 

print_grille(grille)








