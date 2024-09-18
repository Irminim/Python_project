from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    position = db.Column(db.String(50))
    age = db.Column(db.String(3))

    def __init__(self, name, position, age):
        self.name = name
        self.position = position
        self.age = age


with app.app_context():
    db.create_all()


@app.route("/add_employee", methods=["POST"])
def add_employee():
    name = request.form['name']
    position = request.form['position']
    age = request.form['age']
    employee = Employee(name, position, age)
    db.session.add(employee)
    db.session.commit()
    return {"Successfully" :"Employee added successfully"}


@app.route('/get_employee/<int:id>')
def list_employee(id):
    employee = Employee.query.get(id)
    if employee:
        return {
            'id': employee.id,
            'name': employee.name,
            'position': employee.position,
            'age': employee.age
        }
    else:
        return {"error": "Employee is not found"}


if __name__ == "__main__":
    app.run(debug=True)
