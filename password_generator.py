import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    character_pool = ""

    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        return "⚠ You must select at least one character type!"

    password = "".join(random.choice(character_pool) for _ in range(length))
    return password

print("Password Generator")

try:
    num_passwords = int(input("How many passwords do you want to generate? "))
    length = int(input("Enter the desired password length: "))

    print("\nChoose character types to include:")
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include special symbols? (y/n): ").lower() == 'y'

    print("\n Generating passwords...\n")
    for i in range(num_passwords):
        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        print(f"🔑 Password {i+1}: {password}")

except ValueError:
    print("❌ Invalid input. Please enter numeric values for length and count.")
