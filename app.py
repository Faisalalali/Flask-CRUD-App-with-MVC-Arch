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

@app.route('/data/create', methods=['GET','POST'])
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
    return render_template('datalist.html',employees = users)

@app.route('/data/<int:id>')
def RetrieveSingleUser(id):
    user = User.query.filter_by(id=id).first()
    if user:
        return render_template('data.html', user=user)

if __name__ == '__main__':
    app.debug = True
    app.run()