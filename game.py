import board
import os

def attack_row(guess_row,row_size_):
    try:
        if guess_row in range(1,row_size_+1):
            return guess_row
        else:
            print("La coordinata è fuori dal tavolo da gioco")
    except ValueError:
        print("Inserisci un numero")

def attack_col(guess_col,col_size_):
    try:
        if guess_col in range(1,col_size_+1):
            return guess_col
        else:
            print("La coordinata è fuori dal tavolo")
    except ValueError:
        print("Inserisci un numero")


