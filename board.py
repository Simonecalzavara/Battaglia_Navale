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


def board_add(nave,legenda_asse_orizzontale_iniziale,board,row_size,col_size): #metodo che permette l'inserimento di una nave all'interno del tavolo
        while True:
            print("Inserisci la prima coordinata che vuoi inserire della ", nave,"\nLa coordinata inserita rappresenta la testa della nave.")
            coordinate_ = input('Inserisci le coordinate: ')
            col_, rig_ = coordinate_.split()
            for key in legenda_asse_orizzontale_iniziale:
                if legenda_asse_orizzontale_iniziale.get(key) == col_:
                    if col_.isalpha():
                       col = key
                       rig= int(rig_)
                       break
            if board[rig-1][col-1]==0:
                if nave.inserimento(col,rig,row_size,col_size,board)==1:
                    break
            else:
                print("la casella selezionata e'già occupata")



