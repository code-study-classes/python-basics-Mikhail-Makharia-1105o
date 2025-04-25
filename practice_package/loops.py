def sum_even_digits(number):
    total = 0
    for digit in str(abs(number)):
        if int(digit) % 2 == 0:
            total += int(digit)
    return total

def count_vowel_triplets(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    consecutive = 0
    for char in text.lower():
        if char in vowels:
            consecutive += 1
            if consecutive >= 3:
                count += 1
        else:
            consecutive = 0
    return count

def find_fibonacci_index(number):
    a, b = 1, 1
    index = 1
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1

def remove_duplicates(string):
    if not string:
        return ""
    result = string[0]
    for char in string[1:]:
        if char != result[-1]:
            result += char
    return result