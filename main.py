import board as b
from Ship_class import *
from variable import *
from time import sleep

print("Benvenuto ")

#variabili
n_ins=input('Inserisci le dimensioni del tavolo da gioco:  ')
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
print("""\nHai a disposizione 5 navi, puoi inserire ciascuna nave soltanto una volta.
Portaerei, la puoi inserire in 5 caselle
Corazzata, la puoi inserire in 4 caselle
Incrociatore, la puoi inserire in 3 caselle
sottomarino, la puoi inserire in 3 caselle
Cacciatorpediniere la puoi inserire in 2 caselle""")

print("\nLe navi verranno inserite in maniera crescente e secondo la loro dimensione.")
ship_list=[cacciatorpediniere,sottomarino,incrociatore,corazzata,portaerei]
for ship in ship_list:
    b.print_board(board,row_size)
    b.board_add(ship,legenda_asse_orizzontale_iniziale,board,row_size,col_size)
    clearconsole()

b.print_board(board,row_size)

#visualizzazione delle navi piazzate
b.print_board(board_display,row_size)