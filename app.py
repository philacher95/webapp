from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Email
import pymysql



app = Flask(__name__)
app.config["SECRET_KEY"] = "thisisasecret"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://sql2247930:mU1%vW4%@sql2.freemysqlhosting.net/sql2247930'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app, pymysql)


class Inbox(db.Model):
    __tablename__ = "classrequest"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(15))
    lastname = db.Column(db.String(15))
    gender = db.Column(db.String(50))
    email = db.Column(db.String(80))
    phone = db.Column(db.String(10))
    course = db.Column(db.String(20))
    status = db.Column(db.String(15))

    def __init__(self, firstname, lastname, gender, email, phone, course, status):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.phone = phone
        self.course = course
        self.status = status


class registration(FlaskForm):
    firstname = StringField("First Name", validators=[InputRequired("Input required")])
    lastname = StringField("Last Name", validators=[InputRequired("Input required")])
    gender = SelectField("Gender",choices=[("Male", "Male"),("Female", "Female")], validators=[InputRequired("Input required")])
    email = StringField("Email", validators=[InputRequired("Input required"), Email(message="an Invalid Email account name!")])
    phone = IntegerField("Enter Your Phone Number", validators=[InputRequired("Input required")])
    course = SelectField("Select Your Feild",choices=[("COMPUTER HARDWARE", "COMPUTER HARDWARE"),("COMPUTER NETWORKING", "COMPUTER NETWORKING"), ("COMPUTER SOFTWARE", "COMPUTER SOFTWARE")], validators=[InputRequired("Input required")])
    status = TextAreaField("Tell us Your status in I.T", validators=[InputRequired("Input required")])


@app.route("/")
def index():
    return render_template("homepage.html")



@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/about")
def about():
   return render_template("aboutus.html")

@app.route("/register", methods=["POST","GET"])
def register():
    form = registration()
    if form.validate_on_submit():
        #if pymysql.err.OperationalError:
            #flash("Sorry Database is NOT available..!")
            #return redirect(url_for("register"))

        #else:
            new_submit = Inbox(form.firstname.data, form.lastname.data, form.gender.data, form.email.data, form.phone.data, form.course.data, form.status.data)
            db.session.add(new_submit)
            db.session.commit()
            flash("Your Data Has been Submitted Successfully..!")
            return redirect(url_for("register"))
    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
