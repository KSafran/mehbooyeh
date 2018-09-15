"""routes"""
from flask import Blueprint, current_app, render_template, request

BLUEPRINT = Blueprint("BLUEPRINT", __name__)


@BLUEPRINT.route("/")
def sleep():
    return render_template('index.html')


@BLUEPRINT.route('/reg', methods=['POST'])
def reg():
    email = None
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        if not db.session.query(User).filter(User.email == email).count():
            reg = User(username, email)
            db.session.add(reg)
            db.session.commit()
            return render_template('success.html')
    return render_template('index.html')
