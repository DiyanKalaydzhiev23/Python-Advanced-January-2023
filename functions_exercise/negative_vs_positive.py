def print_result(positive, negative):
    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
positive_numbers = sum(n for n in numbers if n > 0)
negative_numbers = sum(n for n in numbers if n < 0)

print_result(positive_numbers, negative_numbers)

# def sum_negative():
#     sum_of_numbers = 0
#
#     for num in numbers:
#         if num < 0:
#             sum_of_numbers += num
#
#     return sum_of_numbers
#
#
# def sum_positive():
#     sum_of_numbers = 0
#
#     for num in numbers:
#         if num > 0:
#             sum_of_numbers += num
#
#     return sum_of_numbers
#
#
# def print_result(positive, negative):
#     print(negative)
#     print(positive)
#
#     if positive > abs(negative):
#         print(f"The positives are stronger than the negatives")
#     else:
#         print(f"The negatives are stronger than the positives")
#
#
# numbers = [int(x) for x in input().split()]
#
# positive_numbers = sum_positive()
# negative_numbers = sum_negative()
#
# print_result(positive_numbers, negative_numbers)
