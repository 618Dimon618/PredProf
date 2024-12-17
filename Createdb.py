from flask import Flask
from models import db, UserGrade, UserType, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()

        usertype1 = UserType(name="Пользователь")
        usertype3 = UserType(name="Администратор")
        db.session.add_all([usertype1, usertype3])

