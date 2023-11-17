from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CityTimeForm(FlaskForm):
    cityID = StringField('City ID', validators=[DataRequired()])
    submit = SubmitField('Get City Time')

class CountryDetailsForm(FlaskForm):
    countryID = StringField('Country ID', validators=[DataRequired()])
    submit = SubmitField('Get Country Details')

class CityDetailsForm(FlaskForm):
    cityID = StringField('City ID', validators=[DataRequired()])
    submit = SubmitField('Get City Details')