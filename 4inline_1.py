import os
from colorama import Fore, Back

def printBlue(data):
    print(Fore.BLUE,data,end="",sep="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")

def printYellow(data):
    print(Fore.YELLOW,data,end="",sep="")

def screenXO(screen):
    os.system('cls')

   
    corners = {
               "upperLeft":     "┌",    #218 np. chr(218)
               "upperRight":    "┐",    #191
               "mediumLeft":    "├",    #195
               "mediumRight":   "┤",    #180
               "bottomLeft":    "└",    #192
               "bottomRight":   "┘",    #217
               "upperMid":      "┬",    #194
               "midiumMid":     "┼",    #197
               "bottomMid":     "┴"     #193
              }
    lines =   {
               "vertical": "│",         #179
               "horizontal": "─"        #196
              }
   
    size = len(screen)                  #rozmiar ekranu

    verticalLine = [lines["horizontal"]*3]*size         #lista zawierająca poziome linie
    # print(verticalLine)
   
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["midiumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)
    # print(verticalUp)
    # print(verticalMid)
    # print(verticalDown)

   

    printBlue(corners["upperLeft"]+verticalUp+corners["upperRight"]+"\n")
 
    for i,row in enumerate(screen):
        printBlue(lines["vertical"])
        for j in row:
            if(j>0): printYellow(" ❤ ")
            elif j<0: printRed(" ❤ ")
            else: printBlue("   ")
            printBlue(lines["vertical"])            
        print()
        if(i < size-1): printBlue(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n")

    printBlue(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")



if __name__ == "__main__":

    rozmiar = 7
    dane = []
    for i in range(rozmiar):
        kolumna = [0 for i in range(rozmiar)]
        dane.append(kolumna)

    zajeteWspolrzedne = []
    czyJest = False  
    y = 6
    gracz = 1

    while True:
        screenXO(dane)
        if gracz == 1: printYellow("Gracz 1\n")
        else: printRed("Gracz 2\n")

        x = int(input("Podaj wsp x: "))
       
       
        a = str(x) + str(y)
       

        for el in zajeteWspolrzedne:
            if str(el) == str(a):
                czyJest = True
                for el in a:
                    y0 = el 
            else:
                pass
       
        if czyJest == False:
            y = 6
        else:
            y = int(y0) - 1
            czyJest = False
           
        a = str(x) + str(y)

        zajeteWspolrzedne.append(a)

        print("zw = ", zajeteWspolrzedne)
       
        dane[y][x] = gracz
        gracz *= -1
