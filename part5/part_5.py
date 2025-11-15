# For your imports look at the rulebook to see what is allowed
# Pour les import permis allez vous référer au livre des règlements
"""part_5.py
This is the template file for the part 5 of the Prelim 1.
Ceci est le fichier template pour la partie 5 du Prelim 1.
"""

def part_5(turns: int, board: [str]):
    """
    Simulate the Game of platypus

    Parameters:
        turns str: The number of turns in the game
        board [str]: The 16x16 grid representing the board of the Game of platypus with x as the platypus and . the food

    Returns:
        str: Is the platypus surviving ("Yes" or "No")
    """

    hunger = 0
    nb_turn = 0
    while hunger < 3 and nb_turn < turns:
        for y,row in enumerate(board):
            for x,el in enumerate(row):
                if el == "x":
                    if board[y][x+1] == ".":
                        hunger = 0
                        board[y][x+1] = "x"
                        board[y][x] = "_"
                        continue
                    if board[y+1][x] == ".":
                        hunger = 0
                        board[y+1][x] = "x"
                        board[y][x] = "_"
                        continue
                    if board[y][x-1] == ".":
                        hunger = 0
                        board[y][x-1] = "x"
                        board[y][x] = "_"
                        continue
                    if board[y][x-1] == ".":
                        hunger = 0
                        board[y-1][x] = "x"
                        board[y][x] = "_"
                        continue
                if el == ".":
                    

                    

                        


    final_answer = "No"
    ### You code goes here ###
    ### Votre code va ici ###




    return final_answer
