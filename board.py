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
        os.system('cls')
        print_board(board, row_size)
        print(player, "Inserisci la prima coordinata della", ship.name,
              "\nLa coordinata inserita rappresenta la testa della nave.",
              "Puoi inserirla in", ship.dimensione, "caselle")
        while True:
            try:
                rig,col=coord_type_change()
                if ship.inserimento(col, rig, row_size, col_size, board, menu.menu()):      #metodo della classe Navi che gestisce l'inserimento delle navi all'interno del tavolo da gioco
                    os.system('cls')
                    break
            except IndexError:
                print("\u001b[31mInserisci una coordinata valida\033[0m\n")
                time.sleep(2)
            except UnboundLocalError:
                print('\u001b[31mInserisci una coordinata sia per le colonne sia per le righe\033[0m\n')
                time.sleep(2)


    return board

def coord_type_change():
    """
    Funzione che consente di cambiare le coordinate inserite in formato numerico
    :return: col: contiene la coordinata associata alle colonne all'interno del tavolo da gioco rig: contiene la coordinata associata alle righe all'interno del tavolo da gioco
    """
    formatted_coordinates=False                                                         #variabile locale che viene assegnata a True solamente nel caso in cui le coordinate vengono inserite nel formato giusto
    while not formatted_coordinates:
        coordinate_ = (input('\nInserisci le coordinate: ')).replace("", " ")
        coordinate = coordinate_.upper()
        if sum(c.isalpha() for c in coordinate) != 1:                                   #check sul numero di coordinate alfabetiche inserite dal giocatore
            print("\u001b[31mInserisci una coordinata per le colonne\033[0m\n")
            continue
        for key in legenda_asse_orizzontale_iniziale:
            try:
                letter = coordinate.find(legenda_asse_orizzontale_iniziale.get(key))
                if legenda_asse_orizzontale_iniziale.get(key) == coordinate[letter]:
                    col = key
                    break
            except ValueError:
                print("\u001b[31mInserisci una coordinata valida per le colonne\033[0m\n")
        numbers = "".join(re.findall(r'\d+', coordinate))                               #regular expression che va a ricercare solamente i digits all'interno delle coordinate inserite dal giocatore
        if numbers != "" :
            rig = int(numbers)
            formatted_coordinates=True
        else:
            print("\u001b[31mInserisci una coordinata valida per le righe\033[0m\n")
            continue

    return rig,col