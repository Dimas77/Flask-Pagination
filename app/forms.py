from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
	post = StringField("post", validators=[DataRequired()])
	submit = SubmitField('Kirim')
	