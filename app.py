from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate

from models.User import User, db
from routes.user_bp import user_bp

app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.before_first_request
def create_tables():
    db.create_all()


app.register_blueprint(user_bp, url_prefix='/users')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/data/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/data')
def RetrieveDataList():
    users = User.query.all()
    return render_template('datalist.html', users=users)

@app.route('/data/view', methods=['GET','POST'])
def viewSelect():
    if request.method == 'GET':
        return render_template('view_select.html')
    if request.method == 'POST':
        id = request.form['id']
        return redirect(url_for('RetrieveSingleUser', id=id))

@app.route('/data/<int:id>')
def RetrieveSingleUser(id):
    user = User.query.filter_by(id=id).first()
    if user:
        return render_template('data.html', user=user)
    return f"Employee with id {id} Doenst exist"

@app.route('/data/update', methods=['GET','POST'])
def updateSelect():
    if request.method == 'GET':
        return render_template('update_select.html')
    if request.method == 'POST':
        id = request.form['id']
        return redirect(url_for('update', id=id))

@app.route('/data/<int:id>/update', methods=['GET','POST'])
def update(id):
    user = User.query.filter_by(id=id).first()
    if request.method == "POST":
        if user:
            user.name = request.form['name']
            user.email = request.form['email']
            user.password = request.form['password']

            db.session.add(user)
            db.session.commit()
            return redirect(url_for('RetrieveSingleUser', id=id))
        return f"Employee with id {id} Does not exist"
    return render_template('update.html', user=user)


@app.route('/data/delete', methods=['GET','POST'])
def deleteSelect():
    if request.method == 'GET':
        return render_template('delete_select.html')
    if request.method == 'POST':
        id = request.form['id']
        return redirect(url_for('delete', id=id))

@app.route('/data/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    user = User.query.filter_by(id=id).first()
    if request.method == "POST":
        if user:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('RetrieveDataList'))
        return f"Employee with id {id} Does not exist"
    return render_template('delete.html', user=user)

if __name__ == '__main__':
    app.debug = True
    app.run()
