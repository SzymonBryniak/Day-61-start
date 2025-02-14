from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email, Length, ValidationError


'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

def is_email(form, field):
    if field.data != "admin@email.com": 
        raise ValidationError('Must be 42')


def is_password(form, field):
    if field.data != "12345678": 
        raise ValidationError('Must be 42')


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(message=' Enter data'), Email(message=('That\'s not a valid email address.')), Length(min=4)])


    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField(label="Log In")

app = Flask(__name__)

app.secret_key = "some secret string"




# form = FlaskForm(meta={'csrf': True})
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print(form.email.data)
    return render_template("login.html", form=form)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)


# MyForm()