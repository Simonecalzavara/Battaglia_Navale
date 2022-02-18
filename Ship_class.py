class Navi:
    # creazione delle navi da gioco

    def __init__(self, dimensione):
        self.dimensione = dimensione
        self.coordinate = []

    #metodo della classe che permette l'inserimento delle coordinate della nave
    def inserimento(self, board, board_display, coord_x, coord_y):
        if not self.coordinate:
            self.coordinate = [[coord_y, coord_x]]
        else:
            self.coordinate.append([coord_y, coord_x])
        board[coord_x - 1][coord_y - 1] = 1
        board_display[coord_y - 1][coord_x - 1] = 1

    #metodo che permette di visualizzare lo stato della nave
    def stato(self):
        if len(self.coordinate) == 0:
            print('la nave é stata affondata')
        elif len(self.coordinate) == self.dimensione:
            print('la nave non é stata colpita')
        elif self.dimensione > len(self.coordinate) > 0:
            print('la nave é stata colpita')