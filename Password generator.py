import random
import string
import os
from datetime import datetime

def generate_random_password(length=12):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def track_password(password, filename="passwords.txt"):
    with open(filename, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {password}\n")

if __name__ == "__main__":
    password_length = 12
    password = generate_random_password(password_length)
    print("Generated Password:", password)
    
    track_password(password)
    print("Password tracked successfully.")
    print(password)

    # os.remove(filename)  # Uncomment to delete the file after tracking the password
