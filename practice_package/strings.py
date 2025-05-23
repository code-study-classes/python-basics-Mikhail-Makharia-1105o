# pylint: disable-all

extract_file_name = lambda full_file_name: full_file_name.split('/')[-1].split('.')[0]


def encrypt_sentence(sentence):
    even_chars = sentence[1::2]
    odd_chars = sentence[0::2][::-1]
    return even_chars + odd_chars


def check_brackets(expression):
    stack = []
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                return i
            stack.pop()
    return -1 if stack else 0


# domain expansion type shi
def reverse_domain(domain):
    parts = domain.split('.')
    return '.'.join(reversed(parts))


def count_vowel_groups(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    count = 0
    in_group = False
    for char in word.lower():
        if char in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    return count