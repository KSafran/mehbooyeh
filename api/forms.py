from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import Required

class MBYForm(FlaskForm):
    name = StringField('name')
    mby = StringField('mby')
