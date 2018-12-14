from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, RadioField
from wtforms.validators import DataRequired, Length


class ZipForm(FlaskForm):
    zipcode = IntegerField(label="Zipcode",
                           validators=[DataRequired(), Length(min=5, max=5)])
    radius = IntegerField(label='Radius', validators=[DataRequired()])
    submit = SubmitField('Find Groups')


