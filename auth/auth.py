from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from .apple import AppleResolver


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        apple_token = request.form['token']
        print(apple_token)
        user = AppleResolver.authenticate(access_token=apple_token)
        return user

    return render_template('login.html')
    # return 'Hello'
