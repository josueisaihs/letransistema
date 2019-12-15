import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, 'carnet', 'listacursodw.csv'), 'r', encoding='ISO-8859-3') as file:
    leer = True
    while leer:
        try:
            nombre, apellido, ci = file.readline().split(",")

            print(nombre, apellido, ci)
        except:
            leer = not leer

    file.close()
    