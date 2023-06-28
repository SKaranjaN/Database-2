from faker import Faker

from app import app
from models import db, Student

with app.app_context():
    
    fake = Faker()

    Student.query.delete()

    students = []
    for i in range(50):
        student = Student(
            name=fake.name(),
            year_joined=fake.year(),
            admission_number=fake.random_int()
        )
        students.append(student)

    db.session.add_all(students)
    db.session.commit()