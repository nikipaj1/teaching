from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class ContactForm(FlaskForm):
    name = StringField('Vardas', [DataRequired()])
    email = StringField("El. pastas", [Email(message=('Neteisingas adresas.')), DataRequired()])
    body = TextAreaField("Jusu Pranesimas", 
                        [DataRequired(), 
                        Length(min=10, message=('Per trumas tekstas'))])
    submit = SubmitField('Submit')