from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///studyDB.db"
db = SQLAlchemy(app)


class Technology(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tech_name = db.Column(db.String(20), unique=True, nullable=False)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(20), unique=False, nullable=False)
    tech_id = db.Column(db.Integer, db.ForeignKey(Technology.id), nullable=False)
    technology = db.relationship("Technology", backref=db.backref("techs", lazy=True))


class Section(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sect_name = db.Column(db.String(50), unique=False, nullable=False)
    parent_sect = db.Column(db.Integer, unique=False, nullable=True)
    cat_id = db.Column(db.Integer, db.ForeignKey(Category.id), nullable=False)
    category = db.relationship("Category", backref=db.backref("categories", lazy=True))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add")
def add():
    # tech = Technology(tech_name="Python")
    # cat = Category(cat_name="django")
    # tech.techs.append(cat)
    # db.session.add(tech)
    # db.session.commit()
    return render_template("add.html")


if __name__ == "__main__":
    db.create_all()

    app.run(debug=True)
