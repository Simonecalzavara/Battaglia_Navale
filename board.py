import time
from variable import legenda_asse_orizzontale_iniziale
import menu
import os
import re

#funzione per visualizzare a schermo il campo da gioco
def print_board(board_array, row_size):
    # Creazione delle coordinate in maniera dinamica
    legenda_asse_orizzontale = ''
    for i in legenda_asse_orizzontale_iniziale:
        legenda_asse_orizzontale += legenda_asse_orizzontale_iniziale[i]
        if i == row_size:
            break
    legenda_asse_orizzontale = " ".join(legenda_asse_orizzontale)
    print("  " + legenda_asse_orizzontale)
    for r in range(row_size):
        print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))
    print()

#funzione che permette l'inserimento di una nave all'interno del tavolo
def board_add(player,ship_list,row_size,col_size):
    board = [[0] * col_size for x in range(row_size)]
    print(player, 'é il tuo turno di inserire le navi')
    time.sleep(3)
    for ship in ship_list:
        while True:
            os.system('cls')
            print_board(board, row_size)
            print(player,"Inserisci la prima coordinata della", ship.name,"\nLa coordinata inserita rappresenta la testa della nave.",
                  "Puoi inserirla in",ship.dimensione,"caselle")
            try:
                coordinate_ = (input('\nInserisci le coordinate: ')).replace(""," ")
                coordinate=coordinate_.upper()
                rig,col=coord_type_change(coordinate)
                if ship.inserimento(col, rig, row_size, col_size, board, menu.menu()):
                    os.system('cls')
                    break
            except IndexError:
                print("\u001b[31mInserisci una coordinata valida\033[0m\n")
                time.sleep(2)
            except UnboundLocalError:
                print('\u001b[31mInserisci una coordinata sia per le colonne sia per le righe\033[0m\n')
                time.sleep(2)


    return board

def coord_type_change(coordinate):
    for key in legenda_asse_orizzontale_iniziale:
        try:
            letter = coordinate.find(legenda_asse_orizzontale_iniziale.get(key))
            if legenda_asse_orizzontale_iniziale.get(key) == coordinate[letter]:
                col = key
                break
        except ValueError:
            print("Inserisci una coordinata alfabetica valida")
    numbers = "".join(re.findall(r'\d+', coordinate))
    rig = int(numbers)

    return rig,col