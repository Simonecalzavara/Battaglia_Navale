menu_options = {
    1: 'Verticale',
    2: 'Orizzontale',
}
#funzione che permette la visualizzazione e l'interazione con il menu di scelta
def print_menu():
    print('\nScegli la maniera con la quale vuoi inserire la tua nave.(Digita il numero della tua scelta)')
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

def option1():
    return 'verticale'

def option2():
    return 'orizzontale'

#funzione che gestisce l'inserimento della scelta da parte dell'utente
def menu():
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('\nInserisci la tua scelta: '))
        except:
            print('Input sbagliato. Inserisci un numero ...')
        if option == 1:
            return option1()
            break
        elif option == 2:
            return option2()
            break
        else:
            print('Opzione invalida.Inserisci un numero tra 1 e 2.')
