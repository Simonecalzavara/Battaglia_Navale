from Ship_class import *
import argparse
import sys
import copy

legenda_asse_orizzontale_iniziale={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'L',11:'M',12:'N',13:'O',14:'P',15:'Q'}
portaerei=Navi(5,"portaerei")
corazzata=Navi(4,"corazzata")
incrociatore=Navi(3,"incrociatore")
sottomarino=Navi(3,"sottomarino")
cacciatorpediniere=Navi(2,"cacciatorpediniere")
numero_navi=5
ship_list=[cacciatorpediniere,sottomarino,incrociatore,corazzata,portaerei]         #creazione della lista delle navi disponibili al giocatore
ship_list_2=copy.deepcopy(ship_list)                                                #creazione di una seconda lista di navi
giocatore1='Giocatore1'
giocatore2='Giocatore2'

def initialize_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--rows",
                        help="Number of rows of the board",
                        type=int,
                        default=9)

    parser.add_argument("-c", "--columns",
                        help="Number of columns of the board",
                        type=int,
                        default=9)


    return parser.parse_args()

def check_parser(args):
    try:
        check_arguments(args)
    except ValueError:
        sys.exit()


def check_arguments(args):
    if not 0 < args.rows < 15:
        print('\u001b[31mInvalid number of rows\033[0m')
        raise ValueError
    if not 0 < args.columns < 15:
        print('\u001b[31mInvalid number of columns\033[0m')
        raise ValueError