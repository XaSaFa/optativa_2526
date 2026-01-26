# programa amb menú que permet tenir una llista d'elements i afegir, eliminar i modificar elements

# variable llista amb tota la informació del meu programa
llista = []

# Funció mostrar_menu mostra les opcions a l'usuari
# li pregunta quina opció vol escollir i retorna el número escollit
def mostrar_menu():
    print("****** MENU ******")
    print("1.- Afegir element")
    print("2.- Eliminar element")
    print("3.- Modificar element")
    print("4.- Mostrar llista d'elements")
    print("5.- Sortir")
    print("******************")
    opcio = int(input("Selecciona una opció: "))
    return opcio

opcio = 0

# Aquesta funció afegeix un element a la llista
def afegir_element():
    element = input("Introdueix el nom de l'element a afegir: ")
    llista.append(element)

# Aquesta funció pregunta un element a l'usuari i l'elimina de la llista
def eliminar_element():
    element = input("Introdueix el nom de l'element a eliminar: ")
    # Controlo l'excepció de que l'element a esborrar no estigui a la llista
    try:
        llista.remove(element)
    except:
        print("L'element introduït no existeix.")

# Aquesta funció mostra els elements de la llista
def mostra_elements():
    for i in llista:
        print(i)

#Aquesta funció pregunta a l'usuari quin element vol modificar
# després quin element nou vol afegir, esborra el vell i afegeix el nou
def modificar_element():
    element_vell = input("Introdueix el nom de l'element a modificar: ")
    element_nou = input("Introdueix el nou nom de l'element: ")
    try:
        llista.remove(element_vell)
        llista.append(element_nou)
    except:
        print("L'element introduït no existeix.")

while True:
    # Mostrem menu
    try:
        opcio = mostrar_menu()
    except:
        opcio = 0
    # Gestionar entrades de l'usuari:
    match opcio:
        case 1:
            # Afegir un element
            afegir_element()
        case 2:
            # Eliminar element
            eliminar_element()
        case 3:
            # Modificar element
            modificar_element()
            pass
        case 4:
            # Mostrar llista d'elements
            mostra_elements()
        case 5:
            # sortir
            print("Gràcies per utilitzar les nostres solucions informàtiques.")
            break
        case _:
            print("La opció seleccionada és incorrecta.")




