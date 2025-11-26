
from api_example import UserSchema, is_valid, export, get_valid_users, write_csv
from test_api_example import min_user
schema = UserSchema()

test = {
        "email": "full@example.com",
        "name": "Mayimus Plenus",
        "age": 65,
        "role": "emperor",
    }
print(not schema.validate(test))