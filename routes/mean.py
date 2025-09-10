from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import DataRequired
class DirectInsc(FlaskForm):
    nom = StringField("nom",
    validators=[DataRequired()])
    mot_passe = PasswordField('mot de passe', validators=[DataRequired()])
    soumettre = SubmitField("s'inscrire")
