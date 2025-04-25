# pylint: disable-all

square_odds = lambda numbers: [x**2 for x in numbers if x % 2 != 0]

normalize_names = lambda names: [name.capitalize() for name in names]


def remove_invalid_emails(emails):
    return [email for email in emails if 
            email.count('@') == 1 and 
            len(email) >= 5 and 
            not email.startswith('@') and 
            not email.endswith('@')]


filter_palindromes = lambda words: [word for word in words if word.lower() == word.lower()[::-1]]


def calculate_factorial(n):
    return 1 if n == 0 else n * calculate_factorial(n - 1)


def find_common_prefix(strings):
    if not strings:
        return ""
    min_len = min(len(s) for s in strings)
    for i in range(min_len):
        char = strings[0][i]
        if any(s[i] != char for s in strings[1:]):
            return strings[0][:i]
    return strings[0][:min_len]