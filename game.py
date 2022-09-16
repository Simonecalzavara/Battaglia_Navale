import board
import os
import time

def hit_guess(board_display,row_size,col_size,ship_list):
    guess=((input("\nInserisci le coordinate per l'attacco: ")).replace(""," ")).upper()
    guess_col,guess_row=board.coord_type_change(guess)
    hit_row=attack_row(guess_row,row_size)
    hit_col=attack_col(guess_col,col_size)
    for ship in ship_list:
        if ship.hit(hit_col,hit_row):
            print("Hai colpito la nave!")
            board_display[guess_col-1][guess_row-1]='*'
            time.sleep(2)
            return True
    print("Non hai colpito nessuna nave")
    board_display[guess_col - 1][guess_row - 1] = 'X'
    time.sleep(2)
    return False


def attack_row(guess_row,row_size_):
    try:
        if guess_row in range(1,row_size_+1):
            return guess_row
        else:
            print("La coordinata è fuori dal tavolo da gioco")
    except ValueError:
        print("Inserisci un numero")

def attack_col(guess_col,col_size_):
    try:
        if guess_col in range(1,col_size_+1):
            return guess_col
        else:
            print("La coordinata è fuori dal tavolo")
    except ValueError:
        print("Inserisci un numero")

# funzione per la gestione del turno del giocatore
def turn(player,ship_list,columns,rows,board_display):
    while True:
        os.system('cls')
        board.print_board(board_display, rows)
        print(player,'é il momento di attaccare\n')
        if hit_guess(board_display, rows, columns,ship_list):
            for ship in ship_list:
                if not ship.coordinate:
                    ship.stato()
                    time.sleep(3)
                    ship_list.remove(ship)
        else:
            break
    return ship_list,board_display

