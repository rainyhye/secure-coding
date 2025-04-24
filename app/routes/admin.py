from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.models import db, User, Product, Report, AdminLog

admin_bp = Blueprint('admin', __name__)


def is_admin():
    user_id = session.get('user_id')
    user = User.query.get(user_id)
    return user and user.role == 'admin'


@admin_bp.route('/admin')
def admin_dashboard():
    if not is_admin():
        flash('관리자 권한이 필요합니다.', 'error')
        return redirect(url_for('auth.login'))

    users = User.query.all()
    products = Product.query.all()
    reports = Report.query.all()
    return render_template('admin/dashboard.html', users=users, products=products, reports=reports)


@admin_bp.route('/admin/block_user/<int:user_id>')
def block_user(user_id):
    if not is_admin():
        flash('권한이 없습니다.', 'error')
        return redirect(url_for('auth.login'))

    user = User.query.get_or_404(user_id)
    user.status = 'blocked'
    db.session.commit()

    log = AdminLog(admin_id=session['user_id'], action=f'Blocked user {user.username}')
    db.session.add(log)
    db.session.commit()

    flash('사용자가 차단되었습니다.', 'success')
    return redirect(url_for('admin.admin_dashboard'))


@admin_bp.route('/admin/block_product/<int:product_id>')
def block_product(product_id):
    if not is_admin():
        flash('권한이 없습니다.', 'error')
        return redirect(url_for('auth.login'))

    product = Product.query.get_or_404(product_id)
    product.is_blocked = True
    db.session.commit()

    log = AdminLog(admin_id=session['user_id'], action=f'Blocked product {product.title}')
    db.session.add(log)
    db.session.commit()

    flash('상품이 차단되었습니다.', 'success')
    return redirect(url_for('admin.admin_dashboard'))
