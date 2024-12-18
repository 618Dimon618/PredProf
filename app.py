from flask import Flask, render_template, request, jsonify
from models import db, Book, User, UserType, UserGrade
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

theme = 'white'


@app.route('/getTheme', methods=['GET'])
def getTheme():
    return {'newTheme': theme}


@app.route('/setTheme', methods=['POST'])
def setTheme():
    global theme
    theme = request.json['newTheme']
    return jsonify(success=True)


@app.route('/egg')
def hello_world():  # put application's code here
    bookList = getBooksByStudent(getStudentsByTeacher('uuuuuuu')[0].nickname)
    print(*[a.title for a in bookList])
    return 'Hello World!'


@app.route('/')
def login():
    return render_template('Войти.html')


@app.route('/profile')
def profile():
    return render_template('index.html')


@app.route('/getKlass', methods=['GET'])
def getKlass():
    studList = getStudentsByTeacher('dinosaur_hunter')
    result = []
    for i in studList:
        temp = getBooksByStudent(i.nickname)
        books = []
        for j in temp:
            books.append({"author": j.author, "title": j.title})
        # books["books_count"] = str(len(temp))
        result.append({'name': i.name, 'last_name': i.last_name, 'books': books, "books_count": len(temp)})
    return result


@app.route('/registration')
def register():
    KvassInfinity = UserGrade.query.all()
    KvassMnogo = UserType.query.all()
    return render_template('Регистрация.html', KvassMnogo=KvassMnogo, KvassInfinity=KvassInfinity)


@app.route('/Kvass1488', methods=['GET', 'POST'])
def confirming1():
    if request.method == 'POST':
        if User.query.filter_by(nickname=request.form['nickname']).first() is None:
            usertype = UserType.query.filter_by(name=request.form['userType']).first()
            usergrade = UserGrade.query.filter_by(name=request.form['userGrade']).first()
            hashed_password = generate_password_hash(request.form['password'])
            user = User(nickname=request.form['nickname'], name=request.form['name'],
                        last_name=request.form['last_name'], password=hashed_password, usertype_id=usertype.id,
                        usergrade_id=usergrade.id)
            db.session.add(user)
            db.session.commit()
            bookshelf = Book.query.all()
            return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf, num=len(bookshelf))
        else:
            return "user already exists"
    if request.method == 'GET':
        return "кто ты?"


def getStudentsByTeacher(teacher):
    teacher = User.query.filter_by(nickname=teacher, usertype_id=2).first()
    if teacher is None:
        return {}
    else:
        return User.query.filter_by(usergrade_id=teacher.usergrade_id, usertype_id=1)


def getBooksByStudent(stud_nickname):
    stud_nickname = User.query.filter_by(nickname=stud_nickname, usertype_id=1).first()
    if stud_nickname is None:
        return {}
    else:
        return Book.query.filter_by(userid=stud_nickname.id).all()


@app.route('/Kvass52', methods=['POST'])
def confirming2():
    user = User.query.filter_by(nickname=request.form['nickname']).first()
    if user is not None:
        hash = generate_password_hash(request.form['password'])
        if check_password_hash(user.password, request.form['password']):
            bookshelf = Book.query.all()
            return render_template('СтраницаФедиЛол.html', bookshelf=bookshelf, num=len(bookshelf))
        else:
            return 'Имя пользователя или пароль указаны неверно'
    else:
        return 'Имя пользователя или пароль указаны неверно'


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
