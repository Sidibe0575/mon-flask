from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, FileField,IntegerField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed
class DirectInsc(FlaskForm):
    nom = StringField("nom",
    validators=[DataRequired()])
    mot_passe= PasswordField("mot de passe", validators=[DataRequired()])
    soumettre = SubmitField("s'inscrire")
class ProduitFormu(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    prix = IntegerField('prix', validators=[DataRequired()])
    image = FileField('image', validators=[FileRequired()]), FileAllowed(['jpg','png'])
    soumettre = SubmitField('ajouter')