from flask_wtf import FlaskForm
from wtforms import StringField,Submitfield,TextAreaField
from wtforms.validators import DataRequireed

class BlogPostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    text = TextAreaField('Text',validators=[DataRequired()])
    submit = SubmitField('Post')