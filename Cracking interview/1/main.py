def cuanto_sale(char, string):
    # funcion que cuenta cuantas veces un caracter char aparece en un string y lo borra
    count = 0
    i = 0
    while i < len(string):
        if char == string[i]:
            count += 1
            # borra char de string cuando lo encuentra
            string = string[0:i] + string[i + 1:len(string)]
        else:
            i += 1
    return count, string


def busqueda(string, string2):
    # compara las veces que aprece un caracter en dos string
    while True:
        # Calcula cuantas veces aparece un caracter
        char = string[0]
        count, string = cuanto_sale(char, string)
        count2, string2 = cuanto_sale(char, string2)
        if count2 != count:
            return False
        if string == "":
            return True


def main():
    # validación
    string = input()
    string2 = input()
    if len(string) != len(string2) or string == string2:
        print(False)
    else:
        resultado = busqueda(string, string2)
        print(resultado)

main()
