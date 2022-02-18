import board as b
from Ship_class import *
from variable import *
from time import sleep
#scelta dell'utente riguardo alle dimensioni della scacchiera

#variabili
n_ins=input('inserisci le dimensioni del tavolo da gioco:  ')
row_size=int(n_ins)
col_size=row_size

#creazione della scacchiera vuota
board = [[0] * col_size for x in range(row_size)]
board_display = [["O"] * col_size for x in range(row_size)]
b.print_board(board_display,row_size)

#clear screen
sleep(2)
clearconsole=lambda: print('\n' * 150)
clearconsole()

#fase di inserimento delle navi
counter_navi=0
while counter_navi<numero_navi:
    print("""\nHai a disposizione 5 navi, puoi inserire ciascuna nave soltanto una volta.
    Portaerei, la puoi inserire in 5 caselle
    Corazzata, la puoi inserire in 4 caselle
    Incrociatore, la puoi inserire in 3 caselle
    sottomarino, la puoi inserire in 3 caselle
    Cacciatorpediniere la puoi inserire in 2 caselle""")
    nave_=input("\n\ninserisci la nave che vuoi piazzare:  ")
    match nave_:
        case "portaerei":
            if counter_p==0:
                b.board_add(portaerei,legenda_asse_orizzontale_iniziale,board,board_display)
                counter_p += 1
            else:
                print("hai gia inserito questa nave. Inserisci una nuova nave")
        case "corazzata":
            if counter_c==0:
                b.board_add(corazzata,legenda_asse_orizzontale_iniziale,board,board_display)
                counter_c+=1
            else:
                print("hai gia inserito questa nave. Inserisci una nuova nave")
        case "incrociatore":
            if counter_i==0:
                b.board_add(incrociatore,legenda_asse_orizzontale_iniziale,board,board_display)
                counter_i+=1
            else:
                print("hai gia inserito questa nave. Inserisci una nuova nave")
        case "sottomarino":
            if counter_s==0:
                b.board_add(sottomarino,legenda_asse_orizzontale_iniziale,board,board_display)
                counter_s=+1
            else:
                print("hai gia inserito questa nave. Inserisci una nuova nave")
        case "cacciatorpediniere":
            if counter_ca==0:
                b.board_add(cacciatorpediniere,legenda_asse_orizzontale_iniziale,board,board_display)
                counter_ca+=1
            else:
                print("hai gia inserito questa nave. Inserisci una nuova nave")
        case _:
            print("inserisci una nave valida.")
    clearconsole()
    b.print_board(board_display, row_size)
    counter_general=[counter_p,counter_c,counter_i,counter_ca,counter_s]
    counter_navi=sum(counter_general)

#visualizzazione delle navi piazzate
b.print_board(board_display,row_size)