import secrets
from string import digits, ascii_letters


def generate_pwd(length=8):
    chars = digits + ascii_letters
    return "".join(secrets.choice(chars) for c in range(length))


def generate_secure_pwd(length=16, upper=3, num_digits=3):
    if length < upper + num_digits + 1:
        raise ValueError("Nice try!")
    while True:
        pwd = generate_pwd(length)
        if (
                any(c.islower() for c in pwd)
                and sum(c.isupper() for c in pwd) >= upper
                and sum(c.isdigit() for c in pwd) >= num_digits
        ):
            return pwd


def get_reset_pwd_url(token_length=16):
    token = secrets.token_urlsafe(token_length)
    return f"https://example.com/reset-pwd/{token}"

