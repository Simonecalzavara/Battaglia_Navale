from Ship_class import Navi
import argparse
import sys
import copy
legenda_asse_orizzontale_iniziale = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I',
                                     10: 'L', 11: 'M', 12: 'N', 13: 'O', 14: 'P', 15: 'Q'}

ship_list = [Navi(2, "cacciatorpediniere"), Navi(3, "sottomarino"), Navi(3, "incrociatore"),
             Navi(4, "corazzata"), Navi(5, "portaerei")]

giocatore1 = 'Giocatore 1'
giocatore2 = 'Giocatore 2'

def initialize_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--rows",
                        help="Numero di righe della griglia",
                        type=int,
                        default=9)

    parser.add_argument("-c", "--columns",
                        help="Numero di colonne della griglia",
                        type=int,
                        default=9)

    parser.add_argument("-s1", "--portaerei",
                        help="Il numero di Portaerei nella tua flotta, se non specificato, è pari a 1. La dimensione di una "
                             "Portaerei è 5.",
                        type=int,
                        default=1)

    parser.add_argument("-s2", "--corazzate",
                        help="Il numero di Corazzate nella tua flotta, se non specificato, è pari a 1. La dimensione di una "
                             "Corazzata è 4",
                        type=int,
                        default=1)

    parser.add_argument("-s3", "--sottomarini",
                        help="Il numero di Sottomarini nella tua flotta, se non specificato, è pari a 1. La dimensione di un "
                             "Sottomarino è 3",
                        type=int,
                        default=1)

    parser.add_argument("-s4", "--incrociatori",
                        help="Il numero di Incrociatori nella tua flotta, se non specificato, è pari a 1. La dimensione di un "
                             "Incrociatore è 3",
                        type=int,
                        default=1)

    parser.add_argument("-s5", "--cacciatorpedinieri",
                        help="Il numero di Cacciatorpedinieri nella tua flotta, se non specificato, è pari a 1. La dimensione di un "
                             "Cacciatorpediniere è 2",
                        type=int,
                        default=1)
    parser.add_argument("-o", "--option",
                        help="La modalitá di gioco desiderata, se 0 (default) i turni finiscono quando il giocatore sbaglia "
                             "altrimenti 1 ",
                        type=int,
                        default=0)

    return parser.parse_args()


def create_ship_list(args):
    """
    Funzione che crea la lista di navi in maniera dinamica in funzione dei parametri di input dei giocatori durante l'avvio del gioco
    :param args: contiene i parametri forniti in input dai giocatori durante l'inizializzazione della sessione di gioco
    :return: restituisce la lista delle navi creata in maniera dinamica
    """
    ship_counts = [args.cacciatorpedinieri, args.incrociatori, args.sottomarini, args.corazzate, args.portaerei]
    ship_list_dynamic = []

    for count, ship in zip(ship_counts, ship_list):
        for _ in range(count):
            ship_list_dynamic.append(copy.deepcopy(ship))

    return ship_list_dynamic


def check_parser(args):
    try:
        check_arguments(args)
    except ValueError:
        sys.exit()


def check_arguments(args):
    if not 0 < args.rows < 15:
        print('\u001b[31mNumero di righe non valido\033[0m')
        raise ValueError
    if not 0 < args.columns < 15:
        print('\u001b[31mNumero di colonne non valido\033[0m')
        raise ValueError
    if not 0 <= args.portaerei <= 2:
        print('\u001b[31mNumero di portaerei non valido\033[0m')
        raise ValueError
    if not 0 <= args.corazzate <= 3:
        print('\u001b[31mNumero di corazzate non valido\033[0m')
        raise ValueError
    if not 0 <= args.sottomarini <= 4:
        print('\u001b[31mNumero di sottomarini non valido\033[0m')
        raise ValueError
    if not 0 <= args.incrociatori <= 5:
        print('\u001b[31mNumero di incrociatori non valido\033[0m')
        raise ValueError
    if not 0 <= args.cacciatorpedinieri <= 5:
        print('\u001b[31mNumero di cacciatorpedinieri non valido\033[0m')
        raise ValueError
    if not (args.option == 0 or args.option == 1):
        print('\u001b[31mModalita di gioco non valida. Seleziona 0 o 1\033[0m')
        raise ValueError