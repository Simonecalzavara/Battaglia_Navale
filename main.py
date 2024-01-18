import os
import time
import board as b
import variable
import game

os.system('cls')

print("Benvenuto ")

args = variable.initialize_parser()
variable.check_parser(args)

#inizializzazione delle liste delle navi dei due giocatori
ship_list_1 = variable.create_ship_list(args)
ship_list_2 = variable.create_ship_list(args)

#creazione del tavolo da gioco per entrambi i giocatori
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

#inserimento delle navi da parte dei due giocatori
board_player_1=b.board_add(variable.giocatore1,ship_list_1,args.rows,args.columns)
board_player_2=b.board_add(variable.giocatore2,ship_list_2,args.rows,args.columns)

#inizio della fase di gioco, la modalita di gioco é selezionata tramite la variabile option passando in ingresso allo script durante l'avvio
game_fin=False
while not game_fin:
    player1, board_display1, game_fin=game.turn(variable.giocatore1, ship_list_2, args.columns, args.rows, board_display1, game_fin, args.option)
    player2, board_display2, game_fin=game.turn(variable.giocatore2, ship_list_1, args.columns, args.rows, board_display2, game_fin, args.option)

print("hai vinto la partita")

print('\nGrazie per aver giocato!')