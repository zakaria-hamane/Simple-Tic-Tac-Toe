# X_X_O____
# string_input = input('Enter cells:').replace("_", " ")
string_input = '_________'.replace("_", " ")


def printGameGrid(string_input):
    print('---------')
    for symbol in range(0, 9, 3):
        grid_line = string_input[symbol:symbol + 3]
        formatted_row = " ".join(grid_line)
        print(f'| {formatted_row} |')
    print('---------')


def strgToList(string_input):
    return list(string_input)


def listToNested(arr):
    arr = strgToList(string_input)
    return [arr[i:i+3] for i in range(0, len(arr), 3)]


def nestedList2List(nested_arr):
    return [item for sublist in nested_arr for item in sublist]


def readCoordinates(user_input):
    return [int(i) for i in user_input.split(" ")]


def coordinatesCheck(coordinates):
    arr = strgToList(string_input)
    nested_arr = listToNested(arr)
    return nested_arr[coordinates[0] - 1][coordinates[1] - 1] == ' '


def winCheck(arr, char):
    # Check all possible winning combinations
    matches = [[0, 1, 2], [3, 4, 5],
               [6, 7, 8], [0, 3, 6],
               [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]

    return any((arr[matches[i][0]] == char and
                arr[matches[i][1]] == char and
                arr[matches[i][2]] == char) for i in range(8))


def gameState(arr):
    xtotal = arr.count('X')
    ototal = arr.count('O')
    game_result = ''
    if xtotal in [ototal + 1, ototal] or ototal in [xtotal + 1, xtotal]:
        if winCheck(arr, 'O'):
            game_result = "Impossible" if winCheck(arr, 'X') else "O wins"
        elif winCheck(arr, 'X'):
            game_result = "Impossible" if winCheck(arr, 'O') else "X wins"
        elif not winCheck(arr, 'O') and not winCheck(arr, 'X'):
            if " " not in arr:
                game_result = "Draw"
            # else:
            #     print("Game not finished")
    else:
        game_result = "Impossible"
    return game_result


printGameGrid(string_input)
while True:
    user_input = input("Enter the coordinates: ")
    if any(i.isalpha() for i in user_input):
        print("You should enter numbers!")
    elif any(int(i) > 3 for i in user_input.split(" ")):
        print("Coordinates should be from 1 to 3!")
    else:
        coordinates = readCoordinates(user_input)
        if coordinatesCheck(coordinates):
            arr = strgToList(string_input)
            nested_arr = listToNested(arr)
            xtotal = arr.count('X')
            ototal = arr.count('O')
            if xtotal == ototal:
                nested_arr[coordinates[0] - 1][coordinates[1] - 1] = "X"
            elif xtotal == ototal + 1:
                nested_arr[coordinates[0] - 1][coordinates[1] - 1] = "O"
            flat_list = nestedList2List(nested_arr)
            string_input = "".join(flat_list)
            printGameGrid(string_input)
            if gameState(flat_list) == "Draw" or gameState(flat_list) == "X wins" or gameState(flat_list) == "O wins":
                print(gameState(flat_list))
                break
        else:
            print("This cell is occupied! Choose another one!")
