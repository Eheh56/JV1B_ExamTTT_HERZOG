#4. Écrire la fonction vérifiant si la grille est complète.
#Elle prend un tableau en entrée, et renvoie un booléen en sortie grâce à l’instruction return.



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
while victoire == 0 :
        X = "X"
        O = "O"
        PX = 1
        PO = 2
        
        player = int(input("voulez vous jouer 'Joueur X' = 1 ou 'joueur O' = 2 ? "))
        print("\n", player)



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

        if grille[0] and grille[1] and grille[2] and grille[3] and grille[4] and grille[5] and grille[6] and grille[7] and grille[8] == (X or O):
            victoire = 2
    

if victoire == 1:
    print("\n \n gg") 
elif victoire == 2:
    print("\n \n vous avez perdu.") 





