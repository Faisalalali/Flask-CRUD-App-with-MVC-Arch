from flask import render_template, request, redirect, url_for, abort

from models.User import User

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def index():
    return render_template('index.html')


def userList():
    users = User.query.all()
    return render_template('datalist.html', users=users)


def create():
    return render_template('createpage.html', user_id=(User.query.count() + 1))


def store():
    if User.query.filter_by(email=request.form['email']).all() != []:
        return render_template('error/emailtaken.html')

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    user = User(name, email, password, phone)
    db.session.add(user)
    db.session.commit()

    return redirect(url_for('user_bp.index'))


def show(user_id):
    # TODO try with .first()
    user = User.query.get(user_id)
    if not user:
        return render_template('usernotfound.html')
    return render_template('show.html', user=user)


def update(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return render_template('usernotfound.html')
    if request.form['email'] != user.email:
        if User.query.filter_by(email=request.form['email']).all() != []:
            return render_template('error/emailtaken.html')

    user.name = request.form['name']
    user.email = request.form['email']
    user.password = request.form['password']
    user.phone = request.form['phone']
    print(f'{user.name} {user.email} {user.password} {user.phone}')
    # User.query.filter_by(user_id=user_id).update(User(user.name, user.email, user.password, user.phone))
    record = db.session.query(User).filter_by(user_id=user_id).first()
    record.name = user.name
    record.email = user.email
    record.password = user.password
    record.phone = user.phone

    db.session.commit()

    return redirect(url_for('user_bp.show', user_id=user_id))


def edit(user_id):
    user = User.query.get(user_id)
    if not user:
        return render_template('usernotfound.html')
    return render_template('update.html', user=user)


def delete(user_id):
    user = User.query.get(user_id)
    if not user:
        return render_template('usernotfound.html')

    if request.method == 'GET':
        return render_template('delete.html', user=user)
    elif request.method == 'POST':
        user = User.query.get(user_id)
        user = db.session.merge(user)
        db.session.delete(user)
        db.session.commit()

        return redirect(url_for('user_bp.index'))


def viewSeceltion():
    if request.method == 'GET':
        return render_template('viewselection.html')
    elif request.method == 'POST':
        user_id = request.form['id']
        return redirect(url_for('user_bp.show', user_id=user_id))


def updateSelection():
    if request.method == 'GET':
        return render_template('updateselection.html')
    elif request.method == 'POST':
        user_id = request.form['id']
        return redirect(url_for('user_bp.update', user_id=user_id))


def deleteSelection():
    if request.method == 'GET':
        return render_template('deleteselection.html')
    elif request.method == 'POST':
        user_id = request.form['id']
        return redirect(url_for('user_bp.delete', user_id=user_id))
