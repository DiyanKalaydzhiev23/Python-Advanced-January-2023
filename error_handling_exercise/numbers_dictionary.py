numbers_dictionary = {}

line = input()
while line != "Search":
    try:
        number_as_string = line
        number = int(input())  # input == two
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

    line = input()

line = input()
while line != "Remove":
    try:
        searched = line
        print(numbers_dictionary[searched])  # {"one": 1} => nums_dict["two"] => KeyError
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

line = input()
while line != "End":
    try:
        searched = line
        del numbers_dictionary[searched] # {"one": 1} => del nums_dict["two"] => KeyError
    except KeyError:
        print("Number does not exist in dictionary")

    line = input()

print(numbers_dictionary)
