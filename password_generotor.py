import random

h = ''' We are Generate a random password containing letters, digits, and special characters.'''
def generate_password(length=12):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{}|;:,.<>?/"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print(h.__doc__)
    print("Generated Password:", generate_password(16))