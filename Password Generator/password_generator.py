import random
import string

def generate_strong_password(length):
    strong_password = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.sample(strong_password , length))
    return password
length = int(input("Enter the length of the Password: "))

password = generate_strong_password(length)
print("Generated Password:", password)
