import os
import random
from colorama import Fore, Back

def printBlue(data):
    print(Fore.BLUE,data,end="",sep="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")

def printYellow(data):
    print(Fore.YELLOW,data,end="",sep="")

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')  # Czyszczenie konsoli

   
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
   
    size = len(board)                  #rozmiar ekranu

    verticalLine = [lines["horizontal"]*3]*size         #lista zawierająca poziome linie
    # print(verticalLine)
   
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["midiumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)
    # print(verticalUp)
    # print(verticalMid)
    # print(verticalDown)

   

    printBlue(corners["upperLeft"]+verticalUp+corners["upperRight"]+"\n")
 
    for row in board:
        printBlue(lines["vertical"])
        for j in row:
            if j==1: printYellow(" ❤ ")
            elif j==-1: printRed(" ❤ ")
            else: printBlue("   ")
            printBlue(lines["vertical"])            
        print()

        if(j < size-1): printBlue(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n")

    printBlue(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")


def check_win(board, player, row, col):
    # Sprawdzanie poziomo
    for c in range(col - 3, col + 1):
        if c >= 0 and c + 3 < len(board[row]):
            if all(board[row][c + i] == player for i in range(4)):
                return True

    # Sprawdzanie pionowo
    for r in range(row - 3, row + 1):
        if r >= 0 and r + 3 < len(board):
            if all(board[r + i][col] == player for i in range(4)):
                return True

    # Sprawdzanie po skosie "/"
    for i in range(4):
        r = row + i
        c = col - i
        if r >= 3 and r < len(board) and c >= 0 and c + 3 < len(board[r]):
            if all(board[r - i][c + i] == player for i in range(4)):
                return True

    # Sprawdzanie po skosie "\"
    for i in range(4):
        r = row - i
        c = col - i
        if r >= 0 and r + 3 < len(board) and c >= 0 and c + 3 < len(board[r]):
            if all(board[r + i][c + i] == player for i in range(4)):
                return True

    return False

def play_game():
    rows = 6
    cols = 6
    board = [[0] * cols for i in range(rows)]
    gracz = 1

    while True:
        print_board(board)

        if gracz == 1:
            printYellow("Gracz 1\n")

            col = int(input("Wybierz kolumne (0-6): "))

           
            for row in range(rows - 1, -1, -1):
                if board[row][col] == 0:
                    board[row][col] = gracz
                    if check_win(board, gracz, row, col):
                        print_board(board)
                        printYellow("Gratulacje wygrales!")
                        return
                    gracz *= -1
                    break
           
        else:
            printRed("Gracz 2\n")

           
            col = [random.randint(0,5)]
            col = col[0]
           
            for row in range(rows - 1, -1, -1):
                if board[row][col] == 0:
                    board[row][col] = gracz
                    if check_win(board, gracz, row, col):
                        print_board(board)
                        printRed("Wygrywa komputer!")
                        return
                    gracz *= -1
                    break
           
       
       
play_game()