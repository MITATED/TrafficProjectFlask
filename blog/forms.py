from wtforms import Form, StringField, TextAreaField
from flask_ckeditor import CKEditorField
from wtforms.validators import DataRequired

class PostForm(Form):
	title = StringField('Title')
	# body = TextAreaField('Body')
	body = CKEditorField('Body', validators=[DataRequired()])
