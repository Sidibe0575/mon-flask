from flask import Blueprint,render_template
from mod import obtenir_produits
utiliser = Blueprint('user', __name__)
@utiliser_bp.route('/utilisera')
def catalogue():
    produits = obtenir_produits()
    return render_template('catalogue.html',
    produits=produits)