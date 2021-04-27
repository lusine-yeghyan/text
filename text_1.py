#1
def chess(x0, x1, y0, y1):
    if abs(x0 - x1) >= 1 and abs(y0 - y1) >= 1:
        return True
    else:
        return False

#2
def run(x, y):
    for i in range(1, y):
        x = x + (x * 10/100)
        z = x * y
        return z
print((run(5, 10)))

#3
def triangle(a, b, c):
    if a == b == c:
        print('հավասարակողմ եռանկյուն')
    elif a == b or b == c or c == a:
        print('հավասարասրուն եռանկյուն')
    elif a + b < c or b + c < a or a + c < a:
        print('գոյություն չունեցող եռանկյուն')
    else:
        print('սովորական եռանկյուն')

#4 նահանջ տարի
def leap(year):
    if year % 4 == 0 and year % 100 != 0:
        return year, 'Leap Year'
    elif year % 400 == 0:
        return year, 'Leap Year'
    elif year % 100 == 0:
        return year, 'Not a Leap Year'
    else:
        return year, "Leap Year"
print('enter any year, but not only 2021: ', leap(2021))

def chingachung(player1, player2):
    if player2 == player1:
        return 'vin together'
    elif (player1 == 'paper' and player2 == 'stone') or (player1 == "scissors" and player2 == 'paper') or (player1 =='stone' and player2 == 'scissors'):
        return 'player1', 'is the winner'
    else:
        return 'player2', 'is the winner'

print(chingachung('paper', 'paper'))
print(chingachung('paper', "scissors"))