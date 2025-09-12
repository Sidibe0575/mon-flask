from flask import Flask, render_template,request,redirect
from flask_wtf import CSRFProtect
import secrets
from flask import Blueprint
from flask import session, url_for
from routes import admin_routes
from flask_wtf import CSRFProtect
from routes.admin_routes import admin_bp
import sqlite3
app =  Flask(__name__)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.config['SECRET_KEY'] = "manzo2025madissou"
activation_csrf = CSRFProtect(app)
@app.route('/index', methods=['POST','GET'])
def identifier():
    return render_template('index.html')
@app.route('/afficher')
def affiche():
    nom = request.form['nom']
    prenom = request.form['prenom']
    numero = request.form['numero']
    centre_interet = request.form['centre d\'interet']
    conn = sqlite3.connect('clients.db')
    curseur = conn.cursor()
    curseur.execute("INSERT INTO clients nom, prenom,numero VALUES (nom, prenom, numero)")
    curseur.commit()
    curseur.close()
    return redirect(url_for('nous.html'))
if __name__ == '__main__':
    port = int(os.environ.get("port", 5000))
    app.run(debug=True, port=port)