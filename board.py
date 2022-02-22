#funzione per visualizzare a schermo il campo da gioco
def print_board(board_array, row_size):
    # creazione del tavolo da gioco vuoto
    legenda_asse_orizzontale_iniziale = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I',
                                         10: 'L', 11: 'M', 12: 'N', 13: 'O', 14: 'P', 15: 'Q'}

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


def board_add(nave,legenda_asse_orizzontale_iniziale,board,board_display):
    i=0
    while i < nave.dimensione:
        try:
            coordinate_ = input('inserisci le coordinate della nave che vuoi piazzare: ')
            x_, y_ = coordinate_.split()
            for key in legenda_asse_orizzontale_iniziale:
                if legenda_asse_orizzontale_iniziale.get(key) == x_:
                    if x_.isalpha():
                        x = key
                        y = int(y_)
                        i=i+1
                        break
            nave.inserimento(board, board_display, x, y)
        except:
            print("inserisci come prima coordinata la coordinata alfabetica")


