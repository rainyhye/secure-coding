# app/routes/dashboard.py
from flask import Blueprint, render_template, session, redirect, url_for, flash
from app.models.models import User, Product

user_bp = Blueprint('dashboard', __name__)

@user_bp.route('/dashboard')
def user_dashboard():
    if 'user_id' not in session:
        flash('로그인이 필요합니다.', 'error')
        return redirect(url_for('auth.login'))

    user = User.query.get(session['user_id'])
    my_products = Product.query.filter_by(seller_id=user.id).all()

    return render_template('dashboard.html', user=user, products=my_products)
