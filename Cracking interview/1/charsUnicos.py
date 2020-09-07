#Engels Miranda
#05/09/2020
#Regresa si no se repiten valores

def buscarIguales(string):
    for i in range(len(string)):
        j=i+1
        for n in range(j,len(string)):
            if string[i]==string[n]:
                return False
    return True
    
def main():
    string = input()
    Resultado = buscarIguales(string)
    print(Resultado)

main()