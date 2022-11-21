import os
import time
import board as b
import variable
import game

os.system('cls')

print("Benvenuto ")

args = variable.initialize_parser()
variable.check_parser(args)
board_display1 = [["O"] * args.columns for x in range(args.rows)]
board_display2 = [["O"] * args.columns for x in range(args.rows)]

#fase d'inserimento delle navi
print("""\nHai a disposizione 5 navi, puoi inserire ciascuna nave soltanto una volta.
Portaerei, la puoi inserire in 5 caselle
Corazzata, la puoi inserire in 4 caselle
Incrociatore, la puoi inserire in 3 caselle
sottomarino, la puoi inserire in 3 caselle
Cacciatorpediniere la puoi inserire in 2 caselle""")

print("\nLe navi verranno inserite in maniera crescente e secondo la loro dimensione.")
time.sleep(5)

board_player_1=b.board_add(variable.giocatore1,variable.ship_list,args.rows,args.columns)
board_player_2=b.board_add(variable.giocatore2,variable.ship_list_2,args.rows,args.columns)

game_fin=False
while not game_fin:
    player1, board_display1, game_fin=game.turn(variable.giocatore1, variable.ship_list_2, args.columns, args.rows, board_display1, game_fin)
    player2, board_display2, game_fin=game.turn(variable.giocatore2, variable.ship_list, args.columns, args.rows, board_display2, game_fin)

print("hai vinto la partita")

print('\nGrazie per aver giocato!')