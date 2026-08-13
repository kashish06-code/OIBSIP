# Random Password Generator using Python - 


# Required Modules
import string
import secrets


# Function to Generate Password
def generate_password(length, chrs):
    password = ''.join(secrets.choice(chrs) for _ in range(length))
    return f"Generated Password: {password}"

try:
    characters = string.ascii_letters + string.digits + string.punctuation  # Character pool
    length = int(input("Enter password length(8-15):"))   # Getting password length

    if length < 8 or length > 15:
        raise ValueError("Password length must be b/w (8-15)!")
    
    pwd = generate_password(length, characters)
    print(pwd)


except ValueError as e:
    print("Error!", e)
