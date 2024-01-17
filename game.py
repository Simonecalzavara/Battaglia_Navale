import board
import os
import time

def hit_guess(board_display,row_size,col_size,ship_list):
    """
    :param board_display: tavolo da gioco del giocatore
    :param col_size: dimensione massima delle colonne del tavolo da gioco
    :param row_size: dimensione massima delle righe del tavolo da gioco
    :param ship_list: lista con le navi piazzate dall'avversario
    :return: True se è stata colpita una nave altrimenti False
    """
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
    """

    :param guess_row: valore della riga scelta dal giocatore attaccante
    :param row_size_: dimensione massima delle righe del tavolo da gioco
    :return: se la coordinata per l'attacco è all'interno del tavolo da gioco allora restituisce la coordinata stessa altrimenti deve essere reinserita
    """
    try:
        if guess_row in range(1,row_size_+1):
            return guess_row
        else:
            print("La coordinata è fuori dal tavolo da gioco")
    except ValueError:
        print("Inserisci un numero")

def attack_col(guess_col,col_size_):
    """

    :param guess_col: valore della colonna scelta dal giocatore attaccante
    :param col_size_: dimensione massima delle colonne del tavolo da gioco
    :return: se la coordinata per l'attacco è all'interno del tavolo da gioco allora restituisce la coordinata stessa altrimenti deve essere reinserita
    """
    try:
        if guess_col in range(1,col_size_+1):
            return guess_col
        else:
            print("La coordinata è fuori dal tavolo")
    except ValueError:
        print("Inserisci un numero")

def turn(player,ship_list,columns,rows,board_display,game_fin):
    """

    :param player: giocatore che deve colpire
    :param ship_list: lista delle navi disponibili del giocatore
    :param columns: n di colonne presenti all interno del tavolo
    :param rows: n di righe presenti all interno del tavolo
    :param board_display: tavolo da gioco del giocatore
    :param game_fin: variabile per la gestione della fine della partita. True se la partita è finita altrimenti è False
    :return: ship_list: ritorna la lista delle navi dell'avversario dopo la fase di attacco del giocatore
    :return: game_fin: valore booleano che indica se la partita è finita o meno
    :return: board_display: tavolo da gioco con marcati i colpi andati a segno o mancati
    """
    while True and not game_fin:
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
        game_fin=win(ship_list,game_fin)
    return ship_list,board_display,game_fin

def win(ship_list,game_fin):
    """

    :param ship_list: lista delle navi del giocatore avversario
    :param game_fin: variabile per la gestione della partita. True se la partita è finita altrimenti è False
    :return: se la lista delle navi dell'avversario è vuota ritorna game_fin True altrimenti False
    """
    if not ship_list:
        game_fin=True
        return game_fin
    return game_fin