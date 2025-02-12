import random
import string


def generate_password(length):
    if length < 6 or length > 32:
        raise ValueError("Довжина пароля має бути від 6 до 32 символів")

    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+="

    while True:
        password = ''.join(random.choice(all_chars) for _ in range(length))

        if (any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in "!@#$%^&*()-_+=" for c in password)):
            return password


def main():
    try:
        num_passwords = int(input("Скільки паролів потрібно згенерувати? "))
        passwords = []

        for i in range(num_passwords):
            length = int(input(f"Введіть довжину пароля {i + 1}: "))
            passwords.append(generate_password(length))

        print("\nЗгенеровані паролі:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}: {pwd}")

    except ValueError as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()