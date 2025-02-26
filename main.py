import random
import string
from typing import Optional

VALID_CHARS = string.digits + string.ascii_letters + string.punctuation

def generate_password(
    length: Optional[int] = 16,
    letters: Optional[int] = None,
    digits: Optional[int] = None,
    punctuation: Optional[int] = None,
):
    password = []
    if letters:
        password.extend(random.choices(string.ascii_letters, k=letters or length))
    if digits:
        password.extend(random.choices(string.digits, k=digits or length))
    if punctuation:
        password.extend(random.choices(string.punctuation, k=punctuation or length))

    random.shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    generated_password = generate_password(
        letters=6,
        digits=3,
        punctuation=1,
    )
    print(f"Generated password: ", generated_password)
