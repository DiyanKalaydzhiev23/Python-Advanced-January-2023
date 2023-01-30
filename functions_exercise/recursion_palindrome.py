def palindrome(word, left_index, right_index=-1):
    if left_index == len(word) // 2:
        return f"{word} is a palindrome"

    if word[left_index] != word[right_index]:
        return f"{word} is not a palindrome"

    return palindrome(word, left_index + 1, right_index - 1)
