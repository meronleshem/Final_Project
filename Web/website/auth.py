from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<p1>Login Page</p1>"

@auth.route('/logout')
def logout():
    return "<p1>Logout</p1>"

@auth.route('/sign-up')
def sign_up():
    return "<p1>Sign Up</p1>"