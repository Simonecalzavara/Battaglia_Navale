class Navi:
    # creazione delle navi da gioco

    def __init__(self, dimensione):
        self.dimensione = dimensione
        self.coordinate = []

    #metodo della classe che permette l'inserimento delle coordinate della nave
    def inserimento(self, coord_col, coord_rig,row_size,col_size,board):
        orientamento_=input("Inserisci la maniera con cui vuoi inserire la nave. Orizzontalmente o Verticalmente?\n\nInserisci una delle due scelte: ")
        orientamento=orientamento_.casefold()
        index=0
        match orientamento:
            case "orizzontalmente":
                if coord_rig in range(row_size):
                    while index in range(self.dimensione) :
                        if coord_col + index in range(col_size):   #inserimento delle coordinate in maniera automatica. Inserisce verso dx
                            self.coordinate.append([coord_col+index,coord_rig])
                            index=index+1
                else:
                    print("\nLa coordinata e' fuori dalla scacchiera. Inserisci una coordinata valida")
            case "verticalmente":
                if coord_col in range(col_size):
                    while index in range(self.dimensione):
                        if coord_rig + index in range(row_size):   #inserimento delle coordinate in maniera automatica. Inserisce verso il basso
                            self.coordinate.append([coord_col,coord_rig+index])
                            index=index+1
                else:
                    print("\nLa coordinata e' fuori dalla scacchiera. Inserisci una coordinata valida")
            case _:
                print("\nInserisci il valore corretto di inserimento. Orizzontalmente o Verticalmente")
        if not self.esiste_posizione(board):
            if len(self.coordinate)==self.dimensione:
                self.riempimento(board)
                return 1
        else:
            self.coordinate=[]
            print("\nLa nave che stai inserendo colliderebbe con un alta nave giá piazzata. Inserisci la prima coordinata della nave in una casella valida.")

    #metodo che permette di visualizzare lo stato della nave
    def stato(self):
        if len(self.coordinate) == 0:
            print('la nave é stata affondata')
        elif len(self.coordinate) == self.dimensione:
            print('la nave non é stata colpita')
        elif self.dimensione > len(self.coordinate) > 0:
            print('la nave é stata colpita')

    def riempimento(self,board):      #riempimento del tavolo con le coordinate inserite della nave
        for coordinate_rig,coordinate_col in self.coordinate:
            board[coordinate_col - 1 ][coordinate_rig - 1]=1

    def esiste_posizione(self,board):      #funzione che restituisce se tutte le coordinate della nave sono presenti all'interno del tavolo
        for coordinate_rig,coordinate_col in self.coordinate:
            if board[coordinate_col-1][coordinate_rig-1]==1:
                return True
        return False