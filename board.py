from variable import legenda_asse_orizzontale_iniziale

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


def board_add(nave,board,row_size,col_size): #metodo che permette l'inserimento di una nave all'interno del tavolo
        while True:
            print("Inserisci la prima coordinata che vuoi inserire della ", nave,"\nLa coordinata inserita rappresenta la testa della nave.")
            coordinate_ = (input('Inserisci le coordinate: ')).replace(""," ")
            coordinate=coordinate_.upper()
            rig,col=coord_type_change(coordinate)
            if board[rig-1][col-1]==0:
                if nave.inserimento(col,rig,row_size,col_size,board)==1:
                    break
            else:
                print("la casella selezionata e'già occupata")


def coord_type_change(coordinate):
    for key in legenda_asse_orizzontale_iniziale:
        try:
            letter = coordinate.find(legenda_asse_orizzontale_iniziale.get(key))
            if legenda_asse_orizzontale_iniziale.get(key) == coordinate[letter]:
                col = key
        except ValueError:
            print("Inserisci una coordinata alfabetica valida")
    numbers = [int(num) for num in coordinate.split() if num.isdigit()]
    rig = numbers[0]
    return rig,col
    pass
