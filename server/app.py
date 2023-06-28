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

@app.route("/students", methods= ["GET", "POST"])
def students():
    if request.method == "GET":
        students = Student.query.all()
        all_students = [student.to_dict() for student in students]

        response = make_response(jsonify(all_students), 200)

        return response
    
    elif request.method == "POST":
        name = request.json.get('name')
        year_joined = request.json.get('year_joined')
        admission_number = request.json.get('admission_number')

        new_student = Student(name=name, year_joined=year_joined, admission_number=admission_number)
        db.session.add(new_student)
        db.session.commit()

        new_student_serialized = new_student.to_dict()
        response = make_response(jsonify(new_student_serialized), 201)

        return response


if __name__ == '__main__':
    app.run(port=5555)
