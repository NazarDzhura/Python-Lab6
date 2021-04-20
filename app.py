from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask-user:1050@localhost/lab6flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    author: str = db.Column(db.String(100), nullable=False)
    genre: str = db.Column(db.String(100), nullable=False)
    year_of_publication: int = db.Column(db.Integer(), nullable=False)
    num_of_pages: int = db.Column(db.Integer(), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Book %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        genre = request.form['genre']
        year_of_publication = request.form['year_of_publication']
        num_of_pages = request.form['num_of_pages']
        new_book = Book(name=name, author=author, genre=genre, year_of_publication=year_of_publication,
                        num_of_pages=num_of_pages)

        try:
            db.session.add(new_book)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding that book'

    else:
        books = Book.query.order_by(Book.date_created).all()
        return render_template('index.html', books=books)


@app.route('/delete/<int:id>')
def delete(id):
    book_to_delete = Book.query.get_or_404(id)

    try:
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue deleting that book'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    book = Book.query.get_or_404(id)

    if request.method == 'POST':
        book.name = request.form['name']
        book.author = request.form['author']
        book.genre = request.form['genre']
        book.year_of_publication = request.form['year_of_publication']
        book.num_of_pages = request.form['num_of_pages']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating that book'

    else:
        return render_template('update.html', book=book)


if __name__ == '__main__':
    app.run()
