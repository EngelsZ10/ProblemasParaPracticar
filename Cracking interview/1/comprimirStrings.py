#Engels Miranda
#05/09/2020
#Comprime strings

def Comprimir():
    string = input()
    string2 = ""
    posInicial = -1
    for i in range(len(string)-1):
            if string[i]!= string[i+1]:
                string2 += string[i] + str(i - posInicial)
                posInicial= i
    string2 += string[len(string)-1] + str(len(string)-1 - posInicial)
    if len(string)>len(string2):
        print(string2)
    else:
        print(string)
     

Comprimir()