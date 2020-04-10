from datetime import datetime, date, time, timedelta
def main():
    cont = 0
    formato = "%d/%m/%Y"
    while True:
        cont = cont + 1
        try:
            cumple = input('Introducir cumpleaños {} (dd/mm/aaaa): '.format(cont))
            if cumple == "":
                break

            hoy = date.today()
            hoy = hoy.strftime(formato)

            cumple = datetime.strptime(cumple, formato)
            hoy = datetime.strptime(hoy, formato)

            if hoy >= cumple:
                diferencia = hoy - cumple
                print("Han pasado:", diferencia.days, "días (Porque en meses no supe je)")
            else:
                print("¿Acaso no haz nacido?... vuelvase serio y escriba su cumpleaños")

        except:
            print('Fecha inválida, use el formato')

    return 0


if __name__ == '__main__':
    main()