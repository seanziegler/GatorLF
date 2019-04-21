from flask_wtf import Form
from wtforms import TextField, DateTimeField, SubmitField
from flask_wtf.file import FileField, FileAllowed
import wtforms.validators as validators


class LostForm(Form):
        title = TextField('What did you find?', validators = [validators.DataRequired(), validators.length(10)])
        date = DateTimeField('When did you find it?', validators = [validators.DataRequired()])
        email =  TextField('Enter your email.', validators = [validators.DataRequired(), validators.Email()])
        image = FileField('Upload a picture.', validators = [FileAllowed(['.jpg', '.jpeg', '.png', '.gif'], "Image formats only!")])
        submit = SubmitField()
