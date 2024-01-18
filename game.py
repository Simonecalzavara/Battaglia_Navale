import board
import os
import time

def hit_guess(board_display,row_size,col_size,ship_list):
    """
    Funzione che gestisce i colpi dei giocatori verso le navi dell'avversario.
    :param board_display: tavolo da gioco del giocatore
    :param col_size: dimensione massima delle colonne del tavolo da gioco
    :param row_size: dimensione massima delle righe del tavolo da gioco
    :param ship_list: lista con le navi piazzate dall'avversario
    :return: True se è stata colpita una nave altrimenti False
    """
    #guess=((input("\nInserisci le coordinate per l'attacco: ")).replace(""," ")).upper()
    while True:
        try:
            guess_col, guess_row = board.coord_type_change()    #verifica del corretto inserimento delle coordinate d'attacco
            hit_row=attack_row(guess_row,row_size)
            hit_col=attack_col(guess_col,col_size)
            for ship in ship_list:
                if ship.hit(hit_col, hit_row):                  #verifica se il colpo ha colpito una nave del giocatore avversario
                    print("Hai colpito la nave!")
                    board_display[guess_col - 1][guess_row - 1] = '\u001b[33m*\033[0m'
                    time.sleep(2)
                    return True
            print("Non hai colpito nessuna nave")
            board_display[guess_col - 1][guess_row - 1] = '\u001b[31mX\033[0m'
            time.sleep(2)
            return False
        except IndexError:
            time.sleep(2)
            continue
        except UnboundLocalError:
            print('\u001b[31mInserisci una coordinata sia per le colonne sia per le righe\033[0m\n')
            time.sleep(2)
            continue


def attack_row(guess_row,row_size_):
    """
    Funzione di controllo sulle righe che verifica se la coordinata d'attacco inserita dal giocatore é all'interno del tavolo da gioco
    :param guess_row: valore della riga scelta dal giocatore attaccante
    :param row_size_: dimensione massima delle righe del tavolo da gioco
    :return: se la coordinata per l'attacco è all'interno del tavolo da gioco allora restituisce la coordinata stessa altrimenti deve essere reinserita
    """
    try:
        if guess_row in range(1,row_size_+1):           #condizione che verifica se la coordinata é all'interno del tavolo da gioco
            return guess_row
        else:
            print("La coordinata è fuori dal tavolo da gioco")
    except ValueError:
        print("Inserisci un numero")

def attack_col(guess_col,col_size_):
    """
    Funzione di controllo sulle colonne che verifica se la coordinata d'attacco inserita dal giocatore é all'interno del tavolo da gioco
    :param guess_col: valore della colonna scelta dal giocatore attaccante
    :param col_size_: dimensione massima delle colonne del tavolo da gioco
    :return: se la coordinata per l'attacco è all'interno del tavolo da gioco allora restituisce la coordinata stessa altrimenti deve essere reinserita
    """
    try:
        if guess_col in range(1,col_size_+1):       #condizione che verifica se la coordinata é all'interno del tavolo da gioco
            return guess_col
        else:
            print("La coordinata è fuori dal tavolo")
    except ValueError:
        print("Inserisci un numero")

def turn(player,ship_list,columns,rows,board_display,game_fin,option):
    """
    Funzione che gestisce il funzionamento dei turni di attacco dei giocatori. Le due modalitá di gioco vengono gestite mediante il parametro option,
    se il valore é pari ad 1 i giocatori hanno a disposizione un colpo a turno, altrimenti i giocatori continuano a colpire fino a quando non mancano il bersaglio
    :param player: giocatore che deve colpire
    :param ship_list: lista delle navi disponibili del giocatore
    :param columns: n di colonne presenti all interno del tavolo
    :param rows: n di righe presenti all interno del tavolo
    :param board_display: tavolo da gioco del giocatore
    :param game_fin: variabile per la gestione della fine della partita. True se la partita è finita altrimenti è False
    :param option: variabile che indica la modalita di gioco
    :return: ship_list: ritorna la lista delle navi dell'avversario dopo la fase di attacco del giocatore
    :return: game_fin: valore booleano che indica se la partita è finita o meno
    :return: board_display: tavolo da gioco con marcati i colpi andati a segno o mancati
    """
    if option==0:                                                           #Modalita dove fino a quando non si sbaglia il colpo si continua a colpire il tavolo da fioco dell'avversario
        while True and not game_fin:
            os.system('cls')
            board.print_board(board_display, rows)
            print(player,'é il momento di attaccare\n')
            if hit_guess(board_display, rows, columns,ship_list):           #se il colpo del giocatore ha colpito una nave avversaria ritorna un valore booleano pari a True
                for ship in ship_list:
                    if not ship.coordinate:                                 #viene effettuato un controllo delle coordinate per ciascuna nave, nel caso in cui una nave dell'avversario
                        ship.stato()                                        #non dovesse avere piú coordinate disponibili viene eseguita la rimozione della nave dalla lista
                        for coordinate in ship.coordinate_colpite:
                            coordinate_col=coordinate[0]
                            coordinate_rig=coordinate[1]
                            board_display[coordinate_rig - 1][coordinate_col - 1] = '\u001b[32m*\033[0m'
                        time.sleep(3)
                        ship_list.remove(ship)
            else:
                break
            game_fin=win(ship_list,game_fin)
        return ship_list,board_display,game_fin
    else:                                                                   #modalita di gioco dove si effettua solamente un colpo per turno
        os.system('cls')
        board.print_board(board_display, rows)
        print(player,'é il momento di attaccare\n')
        if hit_guess(board_display, rows, columns,ship_list):               #se il colpo del giocatore ha colpito una nave avversaria ritorna un valore booleano pari a True
            for ship in ship_list:
                if not ship.coordinate:                                     #viene effettuato un controllo delle coordinate per ciascuna nave, nel caso in cui una nave dell'avversario
                    ship.stato()                                            #non dovesse avere piú coordinate disponibili viene eseguita la rimozione della nave dalla lista
                    time.sleep(3)
                    ship_list.remove(ship)
        game_fin=win(ship_list,game_fin)
        return ship_list,board_display,game_fin

def win(ship_list,game_fin):
    """
    Funzione che gestisce la fine della partita. La partita finisce quando la lista delle navi di uno dei due giocatori é vuota.
    :param ship_list: lista delle navi del giocatore avversario
    :param game_fin: variabile per la gestione della partita. True se la partita è finita altrimenti è False
    :return: se la lista delle navi dell'avversario è vuota ritorna game_fin True altrimenti False
    """
    if not ship_list:                                                       #se la lista delle navi dell'avversario é vuota la variabile che gestisce la fine della partita viene assegnata a True
        game_fin=True
        return game_fin
    return game_fin