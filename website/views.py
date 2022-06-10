from email import contentmanager
from multiprocessing import context
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/cart')
@login_required
def cart():
    return render_template("cart.html", user=current_user)

@views.route('/client')
@login_required
def client():
    return render_template("client.html", user=current_user)



