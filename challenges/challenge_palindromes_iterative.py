def is_palindrome_iterative(word):
    if not word:
        return False

    left = 0
    right = len(word) - 1

    while left < right:
        if word[left] != word[right]:
            return False

        left += 1
        right -= 1

    return True
