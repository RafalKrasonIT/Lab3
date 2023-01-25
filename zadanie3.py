
import random
import string

def create_secure_password():
    # losowe wielkie litery
    upper_letters = ''.join(random.choice(string.ascii_uppercase) for i in range(2))
    # losowe małe litery
    lower_letters = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
    # losowe cyfry
    digits = ''.join(random.choice(string.digits) for i in range(2))
    # losowe znaki specjalne
    special_characters = ''.join(random.choice(string.punctuation) for i in range(2))
    # wszystko łączymy w jedną zmienną
    password = upper_letters + lower_letters + digits + special_characters
    # wyciągamy losowe znaki z powyższej zmiennej
    password = ''.join(random.sample(password))