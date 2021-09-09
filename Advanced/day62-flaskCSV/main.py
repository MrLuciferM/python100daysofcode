from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

def generate_ratings(icon):
    ratings = ['✘']+[icon*i for i in range(1,6)]
    return ratings

class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location = StringField(label='Cafe Location in Google Map (URL)', validators=[DataRequired(), URL()])
    opening = StringField(label='Opening Time e.g. 8AM',validators=[DataRequired()])
    closing = StringField(label='Opening Time e.g. 8:30PM',validators=[DataRequired()])
    coffee = SelectField(label='Coffee Rating',choices=generate_ratings('☕️'))
    wifi = SelectField(label='Wifi Strength Rating',choices=generate_ratings('💪'))
    power = SelectField(label='Power Socket Availability',choices=generate_ratings('🔌'))
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        values = []
        for field,value in form.data.items():
            values.append(value)
        # new_cafe = ','.join(values[:7])``
        # print(new_cafe)
        with open('cafe-data.csv','a',newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(values[:7])
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            # print(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
