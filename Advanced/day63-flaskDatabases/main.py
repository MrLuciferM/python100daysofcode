from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True,nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    def __repr__(self) -> str:
        return f"{self.title} - {self.author} - {self.rating}"

db.create_all()


@app.route('/')
def home():
    return render_template('index.html',books=Books.query.all())


@app.route("/add",methods=['GET','POST'])
def add():
    if request.method=='POST':

        book = Books(
            title=request.form['title'],
            author=request.form['author'],
            rating=request.form['rating']
            )
        print(book)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')


@app.route('/edit',methods=['GET','POST'])
def edit():
    if request.method=='POST':
        book_id = request.form["id"]
        book_to_update = Books.query.get(book_id)
        book_to_update.rating = request.form["newrating"]
        db.session.commit()

        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Books.query.get(book_id)
    return render_template("edit.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Books.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

