from flask import url_for, redirect, session
from functools import wraps

from .constants import ALLOWED_EXTENSIONS


def login_required(func):
    """Checks whether the user is logged in"""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('index'))
        return func(*args, **kwargs)
    return decorated_function


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
