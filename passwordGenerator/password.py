import random
import string
import sys

def generate_password(length):

    all_char = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(all_char) for i in range(length))

    return password


password_length = int(sys.argv[1])

generated_password = generate_password(password_length)

print(generated_password)