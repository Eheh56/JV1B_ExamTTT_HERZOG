#5. Écrire un programme permettant de jouer à deux au Tic tac toe.
#Servez-vous des fonctions écrites dans les exercices 1 à 4 !
import random



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


player = 1
robot = 2
print("\n", player)
victoire = 0
answerRobot = 0
while victoire == 0 :
        X = "X"
        O = "O"
        PX = 1
        PO = 2


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
        
        answerRobot = random.randint(1, 9)




        if answerRobot == 1:
                grille[0] = O     
        if answerRobot == 2:
                grille[1] = O 
        if answerRobot == 3:
                grille[2] = O 
        if answerRobot == 4:
                grille[3] = O 
        if answerRobot == 5:
                grille[4] = O 
        if answerRobot == 6:
                grille[5] = O 
        if answerRobot == 7:
                grille[6] = O 
        if answerRobot == 8:
                grille[7] = O 
        if answerRobot == 9:
                grille[8] = O      
            
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


