def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return (first_string, second_string, False)

    first_string = first_string.lower()
    second_string = second_string.lower()

    sorted_str1 = insertion_sort(first_string)
    sorted_str2 = insertion_sort(second_string)

    is_anagram = sorted_str1 == sorted_str2

    return sorted_str1, sorted_str2, is_anagram


def insertion_sort(string):
    chars = list(string)
    for i in range(1, len(chars)):
        key = chars[i]
        j = i - 1
        while j >= 0 and chars[j] > key:
            chars[j + 1] = chars[j]
            j -= 1
        chars[j + 1] = key

    sorted_string = ''.join(chars)
    return sorted_string

