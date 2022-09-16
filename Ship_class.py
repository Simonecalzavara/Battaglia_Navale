class Navi:
    # creazione delle navi da gioco

    def __init__(self, dimensione,name):
        self.dimensione = dimensione
        self.name=name
        self.coordinate = []

    #metodo della classe che permette l'inserimento delle coordinate della nave
    def inserimento(self, coord_col, coord_rig,row_size,col_size,board,orientamento):
        index=0
        match orientamento:
            case "orizzontale":
                if coord_col+self.dimensione-1 in range(1,row_size+1):
                    while index in range(self.dimensione) :
                        if coord_col + index in range(1,col_size+1):   #Inserimento delle coordinate in maniera automatica. Inserisce verso dx
                            self.coordinate.append([coord_col+index,coord_rig])
                            index=index+1
                else:
                    print("\n\u001b[31mLa coordinata è fuori dalla scacchiera. Inserisci una coordinata valida\033[0m")
            case "verticale":
                if coord_rig+self.dimensione-1 in range(1,col_size+1):
                    while index in range(self.dimensione):
                        if coord_rig + index in range(1,row_size+1):   #Inserimento delle coordinate in maniera automatica. Inserisce verso il basso
                            self.coordinate.append([coord_col,coord_rig+index])
                            index=index+1
                else:
                    print("\n\u001b[31mLa coordinata è fuori dalla scacchiera. Inserisci una coordinata valida\033[0m")
            case _:
                print("\nInserisci il valore corretto di inserimento. Orizzontalmente o Verticalmente")
        if not self.esiste_posizione(board):
            if len(self.coordinate)==self.dimensione:
                self.riempimento(board)
                return True
        else:
            self.coordinate=[]
            print("\nLa nave che stai inserendo colliderebbe con un alta nave giá piazzata. Inserisci la prima coordinata della nave in una casella valida.")

    #metodo che permette di visualizzare lo stato della nave
    def stato(self):
        if len(self.coordinate) == 0:
            print('La nave é stata affondata')
        elif len(self.coordinate) == self.dimensione:
            print('La nave non é stata colpita')
        elif self.dimensione > len(self.coordinate) > 0:
            print('La nave é stata colpita')

    def riempimento(self,board):      #riempimento del tavolo con le coordinate inserite della nave
        for coordinate_rig,coordinate_col in self.coordinate:
            board[coordinate_col - 1 ][coordinate_rig - 1]=1

    def esiste_posizione(self,board):      #funzione che restituisce se tutte le coordinate della nave sono presenti all'interno del tavolo
        for coordinate_rig,coordinate_col in self.coordinate:
            if board[coordinate_col-1][coordinate_rig-1]==1:
                return True
        return False

    def hit(self,guess_row,guess_col):      #metodo che elimina le coordinate dalla nave se viene colpita
        if [guess_col,guess_row] in self.coordinate:
            self.coordinate.remove([guess_col,guess_row])
            return True
        return False
