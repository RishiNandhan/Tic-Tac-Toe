from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print("  "+board[1]+"| "+board[2]+" | "+board[3])
    print("------------")
    print("  "+board[4]+"| "+board[5]+" | "+board[6])
    print("------------")
    print("  "+board[7]+"| "+board[8]+" | "+board[9])

def player_input():
    marker=''
    while not(marker=="X" or marker=="O"):
        marker=input("Player 1: Enter your choice of marker (X or O): ").upper()
    if marker=="X":
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return ((board[1]==board[2]==board[3]==mark)or
            (board[4]==board[5]==board[6]==mark)or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[3] == board[5] == board[7] == mark))

def choose_first():
    if random.randint(0,1)==0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board,position):
    if board[position]==" ":
        return True
    else:
        return False

def full_board_check(board):
    if " " in board[1:]:
        return False
    else:
        return True
def player_choice(board):
    a=list(range(1,10))
    position=' '
    while position not in a or not space_check(board,position):
            position=input("Enter your next position (1-9): ")
            return int(position)



def replay():
    return input("Do you want to play again? y/n").lower().startswith('y')

def play_game():
    print("Let the Game begin!!!")
    score = {'Player 1': 0, 'Player 2': 0, 'Tie': 0}
    while True:

        theboard=[' ']*10
        player1_marker,player2_marker=player_input()
        turn=choose_first()
        print(turn +"will go first")

        game_on=True
        while game_on:
            if turn=="Player 1":
                display_board(board=theboard)
                position=player_choice(board=theboard)
                place_marker(board=theboard,marker=player1_marker,position=position)

                if win_check(board=theboard,mark=player1_marker):
                    display_board(board=theboard)
                    print("Congrats! Player1 has won the game")
                    score[turn]+=1
                    game_on=False
                else:
                    if full_board_check(board=theboard):
                        display_board(board=theboard)
                        print(" The game is a Tie!")
                        score['Tie']+=1
                        break
                    else:
                        #display_board(board=theboard)
                        turn="Player 2"
            elif turn=="Player 2":
                display_board(board=theboard)
                position = player_choice(board=theboard)
                place_marker(board=theboard, marker=player2_marker, position=position)

                if win_check(board=theboard, mark=player2_marker):
                    display_board(board=theboard)
                    print("Congrats! Player2 has won the game")
                    score[turn]+=1
                    game_on = False
                else:
                    if full_board_check(board=theboard):
                        display_board(board=theboard)
                        print(" The game is a Tie!")
                        score['Tie']+=1
                        break
                    else:
                        turn = "Player 1"
        if not replay():
            print(score)
            break

if __name__=="__main__":
    play_game()
