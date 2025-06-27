from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

users = {
    "manager": "admin123",
    "staff": "staff123"
}

roles = {
    "manager": "manager",
    "staff": "staff"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

@auth.get_user_roles
def get_user_roles(user):
    return roles.get(user)
