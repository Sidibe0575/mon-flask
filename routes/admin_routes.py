from flask import Flask,render_template,request,redirect,session
from flask import Blueprint,url_for
from mod import init_db, ajouter_produit, obtenir_produit
from forms.mean import DirectInsc
from forms.mean import ProduitFormu
from flask_bcrypt import Bcrypt
import hashlib
import sqlite3
admin_bp = Blueprint('admin_bp', __name__, url_prefix='/admin')
@admin_bp.route('/requete', methods=['POST', 'GET'])
def catalogue():
    if request.method == 'POST':
        nom = request.form['nom']
        prix = int(request.form['prix'])
        image = request.form['image']
        ajouter_produit(nom, prix, image)
    if request.method == 'POST':
        if not session.get('is_admin'):
            return "Acces refuser"
@admin_bp.route('/ajouter', methods=['POST', 'GET'])
def ajouter():
    nom = request.form.get('nom du produit')
    prix = request.form.get('prix')
    image = request.form.get('image')
    print("produit ajouter")
    return redirect(url_for('admin_bp.ajouter'))
@admin_bp.route('/verifier', methods=['POST', 'GET'])
def verifier():
    Nom = request.form.get('Nom')
    mot_de_passe = request.form.get('Mot_passe') 
    if mot_passe == 'Mot_de_passe':
        session['is_admin'] = True
    return redirect(url_for('admin_bp.verifier'))
    return "mot de passe incorrect"
@admin_bp.route('/deconn', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('deconnecte'))
@admin_bp.route('/voire', methods=['POST'])
def traiter():
    form = DirectInsc()
    if form.validate_on_submit():
        nom = form.nom.data
        mot_de_passe = form.password.data
        hasher = Bcrypt.generate_password_hash(mot_passe).decode('utf-8')
        print("inscription reussie avec succes")
    return render_template('publ.html')
import sqlite3
from routes.mean import ProduitFormu
@admin_bp.route('/validation', methods=['POST','GET'])
def publier():
    prod = ProduitFormu()
    if prod.validate_on_submit():
        nom = prod.nom.data
        prix = prod.prix.data
        image = prod.image.data
        print("publication reussie")    
        conn = sqlite3.connect('produits.db')
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS produits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prix INT NOT NULL,
        image file NOT NULL
        )
        ''')
        cursor.execute("INSERT INTO produits (nom,prix,image)VALUES(?,?,?)",(nom,prix,image))
        conn.commit()
        conn.close()
    return render_template('publ.html',prod=prod)