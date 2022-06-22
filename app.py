from flask import Flask, redirect, render_template, request, url_for
from flask_migrate import Migrate

from models.User import User, db
from routes.user_bp import user_bp

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

@app.before_first_request
def create_tables():
    db.create_all()

app.register_blueprint(user_bp, url_prefix='/users')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
