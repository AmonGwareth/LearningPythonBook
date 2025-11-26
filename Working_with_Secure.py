from password_generator_example import generate_pwd, generate_secure_pwd, get_reset_pwd_url

print(generate_secure_pwd())
print(generate_secure_pwd(length=3, upper=1, num_digits=1))

print(get_reset_pwd_url())
