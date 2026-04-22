# ==========================================
# UNIQUE PASSWORD GENERATOR USING PYTHON
# ==========================================

import random
import string
import secrets

def title():
    print("=" * 45)
    print("      SECURE PASSWORD GENERATOR")
    print("=" * 45)

def choose_complexity():
    print("\nSelect Password Complexity:")
    print("1. Letters Only")
    print("2. Letters + Numbers")
    print("3. Letters + Numbers + Symbols")
    
    choice = input("Enter choice (1-3): ")
    return choice

def generate_password(length, choice):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = "!@#$%^&*()-_=+[]{}<>?/"

    if choice == "1":
        chars = letters
    elif choice == "2":
        chars = letters + numbers
    elif choice == "3":
        chars = letters + numbers + symbols
    else:
        return None

    password = ''.join(secrets.choice(chars) for _ in range(length))
    return password

def password_strength(password):
    score = 0

    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()-_=+[]{}<>?/" for c in password):
        score += 1
    if len(password) >= 12:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

def main():
    while True:
        title()

        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Length must be greater than 0.\n")
                continue
        except:
            print("Please enter a valid number.\n")
            continue

        choice = choose_complexity()
        password = generate_password(length, choice)

        if password:
            print("\nGenerated Password :", password)
            print("Password Strength  :", password_strength(password))
        else:
            print("Invalid choice!")

        again = input("\nGenerate another password? (yes/no): ").lower()
        if again != "yes":
            print("\nThank you for using Password Generator!")
            break
        print()

if __name__ == "__main__":
    main()
