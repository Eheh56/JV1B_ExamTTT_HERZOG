#3. Écrire les fonctions vérifiant si oui ou non l’un des joueurs a réussi à aligner 3
#symboles sur une ligne verticale, horizontale, diagonale.
#Elles prennent un tableau en entrée, et renvoient un booléen en sortie grâce à return.



grille = ['1','2','3','4','5','6','7','8','9']


def print_grille(tableau):
    for i in range(9):
        print(tableau[i], end = ' ')
        if(i == 2 or i ==5):
            print("\n")
            print("-----------")
        elif(i != 8):
            print("|", end = ' ') 


print("\n")


player = 0

player = int(input("voulez vous jouer 'Joueur X' = 1 ou 'joueur O' = 2 ? "))
print("\n", player)
victoire = 0

while victoire == 0:
        X = "X"
        O = "O"
        PX = 1
        PO = 2



        if player == 1:
            answer = int(input("\n \n choissisez un chiffre en 1 et 9 : "))

            while answer<1 or answer>9:
                if answer<1 or answer>9:
                    answer = int(input("choissisez un chiffre en 1 et 9 : "))

            if answer == 1:
                grille[0] = X 
            
            if answer == 2:
                grille[1] = X 
            if answer == 3:
                grille[2] = X 
            if answer == 4:
                grille[3] = X 
            if answer == 5:
                grille[4] = X 
            if answer == 6:
                grille[5] = X 
            if answer == 7:
                grille[6] = X 
            if answer == 8:
                grille[7] = X 
            if answer == 9:
                grille[8] = X 

            print(X)

        elif player == 2:
            answer = int(input("choissisez un chiffre en 1 et 9 : "))

            while answer<1 or answer>9:
                if answer<1 or answer>9:
                    answer = int(input("choissisez un chiffre en 1 et 9 : "))

            if answer == 1:
                grille[0] = O 
            
            if answer == 2:
                grille[1] = O 
            if answer == 3:
                grille[2] = O 
            if answer == 4:
                grille[3] = O 
            if answer == 5:
                grille[4] = O 
            if answer == 6:
                grille[5] = O 
            if answer == 7:
                grille[6] = O 
            if answer == 8:
                grille[7] = O 
            if answer == 9:
                grille[8] = O 

            print(X)



            
        if grille[0] and grille[1] and grille[2] == X:
            print("victoire de X !")
            victoire = 1
        else:
            victoire = 0
        if grille[3] and grille[4] and grille[5] == X:
            print("victoire de X !")
            victoire = 1
        else:
            victoire = 0
        if grille[6] and grille[7] and grille[8] == X:
            print("victoire de X !")
            victoire = 1
        else:
            victoire = 0

        if grille[0] and grille[3] and grille[6] == X:
            print("victoire de X !")
            victoire = 1
        else:
            victoire = 0
        if grille[1] and grille[4] and grille[7] == X:
            print("victoire de X !")
            victoire = 1
        else:
            victoire = 0
        if grille[2] and grille[5] and grille[8] == X:
            print("victoire de X !")
            victoire = 1
        else:
            victoire = 0

        if grille[2] and grille[4] and grille[6] == X:
            print("victoire de X !")
            victoire = 1
        else:
            victoire = 0
        
        if grille[0] and grille[4] and grille[8] == X:
            print("victoire de X !")
            victoire = 1
        else:
            victoire = 0

        print(victoire)
        print_grille(grille)

player = int(input("voulez vous jouer 'Joueur X' = 1 ou 'joueur O' = 2 ? "))
print("\n", player)
print("\n \n gg")