import time
from variable import legenda_asse_orizzontale_iniziale
import menu
import os
import re

#funzione per visualizzare a schermo il campo da gioco
def print_board(board_array, row_size):
    """
    Funzione che permette la visualizzazione a schermo del campo da gioco
    :param board_array: array contenente le informazioni relative allo stato del tavolo da gioco del giocatore
    :param row_size: massima dimensione delle righe del tavolo da gioco
    :return: print del tavolo da gioco
    """
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
    """
    Funzione che consente l'inserimento delle navi all'interno del tavolo da gioco
    :param player: variabile associata al giocatore che deve inserire la propria lista di navi all'interno del tavolo da gioco
    :param ship_list: lista delle navi da inserire all'interno del tavolo da gioco
    :param row_size: massima dimensione delle righe del tavolo da gioco
    :param col_size: massima dimensione delle colonne del tavolo da gioco
    :return:
    """
    board = [[0] * col_size for x in range(row_size)]
    print(player, 'é il tuo turno di inserire le navi')
    time.sleep(3)
    for ship in ship_list:
        while True:
            try:
                rig,col=coord_type_change(board,row_size,player,ship.name,ship.dimensione)
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

def coord_type_change(board,row_size,player,ship,dimensione):
    """
    Funzione che consente di cambiare le coordinate inserite in formato numerico
    :param board: stringa contente le coordinate in formato alfanumerico
    :param row_size: massima dimensione delle righe del tavolo da gioco
    :param player: stringa contente il nome del giocatore
    :param ship: tipologia della nave da inserire all'interno del tavolo da gioco
    :param dimensione: dimensione della nave da inserire all'interno del tavolo da gioco
    :return: col: contiene la coordinata associata alle colonne all'interno del tavolo da gioco rig: contiene la coordinata associata alle righe all'interno del tavolo da gioco
    """
    os.system('cls')
    print_board(board, row_size)
    print(player, "Inserisci la prima coordinata della", ship,
          "\nLa coordinata inserita rappresenta la testa della nave.",
          "Puoi inserirla in", dimensione, "caselle")
    formatted_coordinates=False
    while not formatted_coordinates:
        coordinate_ = (input('\nInserisci le coordinate: ')).replace("", " ")
        coordinate = coordinate_.upper()
        for key in legenda_asse_orizzontale_iniziale:
            try:
                letter = coordinate.find(legenda_asse_orizzontale_iniziale.get(key))
                if legenda_asse_orizzontale_iniziale.get(key) == coordinate[letter]:
                    col = key
                    break
            except ValueError:
                print("\u001bInserisci una coordinata valida per le colonne\033[0m\n")
        numbers = "".join(re.findall(r'\d+', coordinate))
        if numbers != "" :
            rig = int(numbers)
            formatted_coordinates=True
        else:
            print("\033[0m\nInserisci una coordinata valida per le righe\033[0m\n")
            continue

    return rig,col