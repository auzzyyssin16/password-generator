import random
import string

def generate_password(length=12, use_numbers=True, use_symbols=True, use_uppercase=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()_+"

    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length: "))
    except ValueError:
        print("Invalid input. Using default length of 12.")
        length = 12

    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase? (y/n): ").lower() == 'y'

    password = generate_password(length, use_numbers, use_symbols, use_uppercase)
    print("\nGenerated password:", password)

    # Save to a text file
    with open("generated_password.txt", "w") as file:
        file.write(password)

    print("Password saved to generated_password.txt")
