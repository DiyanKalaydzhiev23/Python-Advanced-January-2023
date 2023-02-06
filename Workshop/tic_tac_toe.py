import speech_recognition as sr

from collections import deque
from pyfiglet import Figlet


def get_name(player_number):
    while True:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print(f"Player {player_number}, say your name")

            audio_data = r.record(source, duration=3)
            print("Recognizing")

            try:
                return r.recognize_google(audio_data)
            except sr.UnknownValueError:
                print("Please say your name again")


def check_for_draw():
    if all([all(pos.strip() for pos in row) for row in board]):
        print("Draw!")
        raise SystemExit


def check_for_win():
    player_name, player_symbol = players[0]

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(size)])
    second_diagonal_win = all([board[i][size - 1 - i] == player_symbol for i in range(size)])

    row_win = any([all(pos == player_symbol for pos in row) for row in board])
    col_win = any([all(board[r][c] == player_symbol for r in range(size)) for c in range(size)])

    # col_result = []  # [False, True, False]
    #
    # for c in range(size):
    #     current_result = []  # [True, True, True]
    #
    #     for r in range(size):
    #         current_result.append(board[r][c] == player_symbol)
    #
    #     col_result.append(all(current_result))
    #
    # col_win = any(col_result)

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print(f"{player_name} won!")
        raise SystemExit

    players.append(players.popleft())


def place_symbol(position):
    row, col = (position - 1) // size, (position - 1) % size

    if board[row][col] != " ":
        raise ValueError

    board[row][col] = players[0][1]

    print_board()

    check_for_win()
    check_for_draw()

    choose_position()


def choose_position():
    while True:
        try:
            position = int(input(f"{players[0][0]} choose a free position [1-{size * size}]: "))

            if 1 <= position <= size * size:
                place_symbol(position)
                break
            else:
                raise ValueError

        except ValueError:
            print(f"{players[0][0]} enter a valid position!")


def print_board(begin=False):
    if begin:
        print("This is the numeration of the board: ")
        [print(f"| {' | '.join(row)} |") for row in board]
        print(f"{players[0][0]} starts first!")

        for row in range(size):
            for col in range(size):
                board[row][col] = " "
    else:
        [print(f"| {' | '.join(row)} |") for row in board]


def start():
    figlet = Figlet(font='big')
    print(figlet.renderText("Tic-Tac-Toe"))

    player_one_name = get_name("one")
    player_two_name = get_name("two")

    while True:
        player_one_symbol = input(f"{player_one_name} would you like to play with 'X' or 'O'? ").upper()

        if player_one_symbol not in ["X", "O"]:
            print(f"{player_one_name} select a valid option!")
        else:
            break

    player_two_symbol = "O" if player_one_symbol == "X" else "X"

    players.append([player_one_name, player_one_symbol])
    players.append([player_two_name, player_two_symbol])

    print_board(begin=True)
    choose_position()


players = deque()  # [[player one name, player one symbol], [...]]
board = [[str(i), str(i + 1), str(i + 2)] for i in range(1, 10, 3)]
size = len(board)

start()

# pip install pyfiglet
# pip install SpeechRecognition==3.8.1
# pip install pyaudio
