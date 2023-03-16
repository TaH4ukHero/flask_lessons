from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, IntegerField, StringField
from wtforms.validators import DataRequired


class AddJobForm(FlaskForm):
    team_leader = IntegerField("Team Leader ID", validators=[DataRequired()])
    job = StringField("Job title", validators=[DataRequired()])
    work_size = IntegerField("Work size", validators=[DataRequired()])
    collaborators = StringField("Collaborators", validators=[DataRequired()])
    is_finished = BooleanField("Is job finished?")

    submit = SubmitField("Submit")
