import time


class Navi:
    # creazione delle navi da gioco

    def __init__(self, dimensione,name):
        self.dimensione = dimensione
        self.name=name
        self.coordinate = []
        self.coordinate_colpite=[]

    #metodo della classe che permette l'inserimento delle coordinate della nave
    def inserimento(self, coord_col, coord_rig,row_size,col_size,board,orientamento):
        """
        Metodo della classe che permette l'inserimento delle coordinate della nave
        :param coord_col: coordinata delle colonne associate all'inserimento della nave
        :param coord_rig: coordinata delle righe associate all'inserimento della nave
        :param row_size: dimensione del tavolo da gioco associata alle righe
        :param col_size: dimensione del tavolo da gioco associata alle colonne
        :param board: tavolo da gioco associato al giocatore
        :param orientamento: verso d'inserimento della nave. La nave puó essere inserita in maniera vertical o in maniera orizzontale
        :return: Restituisce il valore True se la nave é stata inserita in maniera corretta all'interno del tavolo da gioco, altrimenti False
        """
        index=0
        match orientamento:
            case "orizzontale":
                if coord_col+self.dimensione-1 in range(1,row_size+1):
                    while index in range(self.dimensione) :
                        if coord_col + index in range(1,col_size+1):   #Inserimento delle coordinate in maniera automatica. Inserisce verso dx
                            self.coordinate.append([coord_col+index,coord_rig])
                            index=index+1
                else:
                    print("\n\u001b[31mLa nave verrá piazzata fuori dal tavolo da gioco. Inserisci una coordinata valida\033[0m")
                    time.sleep(3)
            case "verticale":
                if coord_rig+self.dimensione-1 in range(1,col_size+1):
                    while index in range(self.dimensione):
                        if coord_rig + index in range(1,row_size+1):   #Inserimento delle coordinate in maniera automatica. Inserisce verso il basso
                            self.coordinate.append([coord_col,coord_rig+index])
                            index=index+1
                else:
                    print("\n\u001b[31mLa nave verrá piazzata fuori dal tavolo da gioco. Inserisci una coordinata valida\033[0m")
                    time.sleep(3)
            case _:
                print("\nInserisci il valore corretto di inserimento. Orizzontalmente o Verticalmente")
        if not self.esiste_posizione(board) and not self.esiste_vicino(board,col_size,row_size):            #check per verificare che la nave possa essere inserita all'interno del tavolo da gioco
            if len(self.coordinate)==self.dimensione:                                                       #seguendo le regole del gioco
                self.riempimento(board)
                return True
        else:
            self.coordinate=[]
            print("\nLa nave che stai inserendo colliderebbe con un alta nave giá piazzata. Inserisci la prima coordinata della nave in una casella valida.")
            time.sleep(5)

    #metodo che permette di visualizzare lo stato della nave
    def stato(self):
        """
        Metodo della classe Ship che restituisce lo stato della nave
        :return: print dello stato attuale della nave
        """
        if len(self.coordinate) == 0:
            print('La nave é stata affondata')
        elif len(self.coordinate) == self.dimensione:
            print('La nave non é stata colpita')
        elif self.dimensione > len(self.coordinate) > 0:
            print('La nave é stata colpita')

    def riempimento(self,board):      #riempimento del tavolo con le coordinate inserite della nave
        """
        Metodo della classe nave che riempie la scacchiera in base alle coordinate inserite dal giocatore
        :param board: tavolo da gioco del giocatore
        """
        for coordinate_rig,coordinate_col in self.coordinate:
            board[coordinate_col - 1 ][coordinate_rig - 1]=1

    def esiste_posizione(self,board):      #funzione che restituisce se tutte le coordinate della nave sono presenti all'interno del tavolo
        """
        Metodo della nave che restituisce se tute le coordinate della nave sono presenti all'interno del tavolo da gioco
        :param board: tavolo da gioco del giocatore
        :return: True se tutte le coordinate della nave sono presenti all'interno del tavolo da gioco, altrimenti False
        """
        for coordinate_rig,coordinate_col in self.coordinate:
            if board[coordinate_col-1][coordinate_rig-1]==1:
                return True
        return False

    def hit(self,guess_row,guess_col):      #metodo che elimina le coordinate dalla nave se viene colpita
        """
        :param guess_row: coordinata delle righe associata al colpo
        :param guess_col: coordinata delle colonne associata al colpo
        :return: True se una coordinata della nave é stata colpita altrimenti False
        """
        if [guess_col,guess_row] in self.coordinate:
            self.coordinate.remove([guess_col,guess_row])                            #rimozione delle coordinate dalla lista delle coordinate della nave colpita
            self.coordinate_colpite.append([guess_col,guess_row])                    #aggiunta delle coordinate colpite all'interno della lista delle coordinate colpite della nave
            return True
        return False

    def esiste_vicino(self,board,col_size,row_size):                                  #controllo della presenza di navi nel intorno della nave che sta per essere piazzata
        """
        Metodo della classe per effettuare un check sulla presenza di navi vicine durante l'inserimento di una nave sul tavolo da gioco
        :param board: tavolo da gioco del giocatore
        :param col_size: massima dimensione delle colonne del tavolo da gioco
        :param row_size: massima dimensione delle righe del tavolo da gioco
        :return: True se esiste una coordinata di un altra nave vicino alla nave che sta per essere piazzata, altrimenti False
        """
        if self.esiste_vicino_verticale(board,col_size) or self.esiste_vicino_orizzontale(board,row_size):          #viene effettuato un check dei vicini sia verticalmente che orizzontalmente
            return True
        return False

    def esiste_vicino_verticale(self,board,col_size):
        """
        Metodo della classe per effettuare un check verticalmente sulla presenza di navi vicine durante l'inserimento di una nave sul tavolo da gioco
        :param board: tavolo da gioco del giocatore
        :param col_size: massima dimensione delle colonne del tavolo da gioco
        :return: True se esiste una coordinata di un altra nave vicino alla nave che sta per essere piazzata, altrimenti False
        """
        for coordinate_col,coordinate_rig in self.coordinate:
            if coordinate_col== 1 and board[coordinate_rig-1][coordinate_col]==1:                                   #nave inserita nella prima colonna e controllo esistenza nave a destra
                return True
            elif coordinate_col==col_size:                                                                          #nave inserita nell ultima colonna e controllo esistenza nave a sinistra
                if board[coordinate_rig - 1][coordinate_col-2] == 1:
                    return True
            elif board[coordinate_rig - 1][coordinate_col] == 1 and coordinate_col != col_size:                     #controllo esistenza nave a destra durante inserimento
                return True
            elif board[coordinate_rig - 1][coordinate_col - 2] == 1 and coordinate_col != 1:                        #controllo esistenza nave a sinistra durante inserimento
                return True
        return False

    def esiste_vicino_orizzontale(self,board,row_size):
        """
        Metodo della classe per effettuare un check orizzontalmente sulla presenza di navi vicine durante l'inserimento di una nave sul tavolo da gioco
        :param board: tavolo da gioco del giocatore
        :param row_size: massima dimensione delle righe del tavolo da gioco
        :return: True se esiste una coordinata di un altra nave vicino alla nave che sta per essere piazzata, altrimenti False
        """
        for coordinate_col, coordinate_rig in self.coordinate:
            if coordinate_rig == 1 and board[coordinate_rig ][coordinate_col-1] == 1:                               #nave inserita nella prima riga e controllo esistenza nave sotto
                return True
            elif coordinate_rig == row_size:                                                                        #nave inserita nel ultima riga e controllo esistenza nave sopra
                if board[coordinate_rig - 2][coordinate_col - 1] == 1:
                    return True
            elif board[coordinate_rig ][coordinate_col - 1] == 1 and coordinate_rig != row_size:                    #controllo esistenza nave sotto durante inserimento
                return True
            elif board[coordinate_rig - 2][coordinate_col - 1] == 1 and coordinate_rig != 1:                        #controllo esistenza nave sopra durante inserimento
                return True
        return False