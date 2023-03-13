from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,IntegerField,SelectField,SubmitField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

class CreateProperty(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField("Description", validators=[InputRequired()])
    bedrooms = IntegerField('No. of Rooms', validators=[InputRequired()])
    bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired()])
    price = IntegerField('Price', validators=[InputRequired()])
    type = SelectField('Property Type', choices=[('House'), ('Apartment')], validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    image = FileField("Image", validators=[InputRequired(), FileRequired(), FileAllowed(['jpg','jpeg', 'png', 'gif', 'tiff', 'ai', 'raw', 'eps', 'webp', 'avif', 'svg'], 'Images only')])
    submit = SubmitField("Add Property")