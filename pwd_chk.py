import string
import getpass


def check_pwd():
    password = getpass.getpass("Enter Password: ")

    strength = 0
    remarks = ""

    lower_count, upper_count,num_count, wspace_count, special_count = 0, 0, 0, 0, 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char.isspace():
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if wspace_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength <= 1:
        remarks = "Very weak password! Change ASAP."
    elif strength == 2:
        remarks = "Weak password! Consider changing it."
    elif strength == 3:
        remarks = "Moderate password. It can be improved."
    elif strength == 4:
        remarks = "Good password, but it can be better."
    else:
        remarks = "Strong character combination!"

    print("\nYour password has:")
    print(f"{lower_count} lowercase characters")
    print(f"{upper_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{wspace_count} whitespace characters")
    print(f"{special_count} special characters")
    print(f"\nPassword Strength: {strength}/5")
    print(f"Hint: {remarks}")


def ask_pwd(another_pwd=False):
    if another_pwd:
        choice = "Do you want to check another password (y/n): "
    else:
        choice = "Do you want to check a password (y/n): "

    while True:
        choice = input(choice).strip().lower()

        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid input. Please enter y or n.")


if __name__ == "__main__":
    print("=== Welcome to Password Checker ===")

    ask_pw = ask_pwd()

    while ask_pw:
        check_pwd()
        ask_pw = ask_pwd(another_pwd=True)

    print("Thank you for using Password Checker!")
