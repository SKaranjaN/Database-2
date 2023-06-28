from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database-2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
migrate = Migrate(app, db)

db.init_app(app)

@app.route("/")
def Index():
    return f'<h1>Welcome to Database School.</h1>'

if __name__ == '__main__':
    app.run(port=5555)
