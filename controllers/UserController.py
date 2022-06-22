import sys
from flask import render_template, Request, redirect, url_for, abort

from models.User import User

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def index():
    users = User.query.all()
    return render_template('users/index.html', users=users)


def store():
    name = Request.form['name']
    email = Request.form['email']
    password = Request.form['password']

    user = User(name=name, email=email, password=password)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('user_bp.index'))

def show(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)
    return render_template('users/show.html', user=user)

def update(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)

    user.name = Request.form['name']
    user.email = Request.form['email']
    user.password = Request.form['password']
    db.session.commit()

    return redirect(url_for('user_bp.show', user_id=user_id))

def delete(user_id):
    user = User.query.get(user_id)
    if not user:
        abort(404)

    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('user_bp.index'))
    