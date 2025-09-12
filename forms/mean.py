from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, FileField,IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed
class DirectInsc(FlaskForm):
    nom = StringField("nom",
    validators=[DataRequired()])
    mot_passe= PasswordField("mot de passe", validators=[DataRequired()])
    submit= SubmitField("s'inscrire")
class ProduitFormu(FlaskForm):
    nom = StringField('nom', validators=[DataRequired()])
    prix = IntegerField('prix', validators=[DataRequired()])
    image = FileField('image', validators=[FileRequired()]), FileAllowed(['jpg','png'])
    soumettre = SubmitField('ajouter')