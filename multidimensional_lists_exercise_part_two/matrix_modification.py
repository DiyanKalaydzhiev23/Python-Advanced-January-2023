size = int(input())  # прочитаме редовете
matrix = [[int(n) for n in input().split()] for _ in range(size)]
# създаваме матрица от числа, за всеки ред преобразуваме числата от текст в цели числа

command = input().split()  # прочитаме първата команда

while command[0] != 'END':  # проверяваме дали комадата е END, дъно на нашия цикъл
    type_command, row, col, num = command[0], int(command[1]), int(command[2]), int(command[3])
    # прочитаме командата, реда, колоната и числото

    if row < 0 or row >= size or col < 0 or col >= size:  # проверяваме дали координатите са валидни
        print('Invalid coordinates')  # принтираме съобщението invalid coordinates
    elif type_command == 'Add':  # проверяваме дали командата е Add
        matrix[row][col] += num  # добавяме числото към числото на позицията
    elif type_command == 'Subtract':  # проверяваме дали командата е Subtract
        matrix[row][col] -= num  # намаляме числото на позицията с текущото число

    command = input().split()  # четем нова команда

[print(*row) for row in matrix]
# за всеки под-лист в матрицата, ънпакваме реда и го принтираме
