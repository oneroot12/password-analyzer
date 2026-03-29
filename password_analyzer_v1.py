import string


def checksafety(password):

    rating = 0
    reasons = []

    passlength = len(password)
    has_strings = any(c.isalpha() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_symbols = any(c in string.punctuation for c in password)

    if passlength >= 8:
        rating = rating + 1
    else:
        reasons.append("Your password uses less than 8 characters.")

    if has_strings:
        rating = rating + 1
    else:
        reasons.append("Missing letters.")

    if has_digits:
        rating = rating + 1
    else:
        reasons.append("Missing numbers.")

    if has_symbols:
        rating = rating + 1
    else:
        reasons.append("Missing special characters.")

    return rating, reasons


def timetocrack(password):
    charset_size = 0

    if any(c.isalpha() for c in password):
        charset_size = charset_size + 52

    if any(c.isdigit() for c in password):
        charset_size = charset_size + 10

    if any(c in string.punctuation for c in password):
        charset_size = charset_size + 32

    combinations = charset_size ** len(password)

    return combinations


while True:
    password = input("Type the password you want to analyze. ")
    rating, reasons = checksafety(password)
    combinations = timetocrack(password)
    attempts_persec = 1_000_000_000
    bruteforce_time = combinations / attempts_persec

    minutes = bruteforce_time / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365

    if rating <= 2:
        strength = "Weak"
    elif rating == 3:
        strength = "Medium"
    elif rating == 4:
        strength = "Secure"

    print("\nPassword analyzed:", "*" * len(password))

    print("\nStrength:", strength)
    if reasons:
        print(f"Reasons:")
        for reason in reasons:
            print("-", reason)

    if years >= 1:
        print(f"\nExpected time to crack: {round(years, 2)} years.")
    elif days >= 1:
        print(f"\nExpected time to crack: {round(days, 2)} days.")
    elif hours >= 1:
        print(f"\nExpected time to crack: {round(hours, 2)} hours.")
    else:
        print(f"\nInstantly crackable.")

    try_again = input("Try again? Type YES: ").lower()

    if try_again == "yes" or "y":
        continue
    else:
        exit()
