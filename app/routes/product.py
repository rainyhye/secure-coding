from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.models import db, Product, User
from werkzeug.utils import secure_filename
import os

product_bp = Blueprint('product', __name__)

UPLOAD_FOLDER = 'app/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@product_bp.route('/products')
def list_products():
    products = Product.query.filter_by(is_blocked=False).all()
    return render_template('product/list.html', products=products)



@product_bp.route('/products/<int:product_id>')
def view_product(product_id):
    product = Product.query.get_or_404(product_id)
    if product.is_blocked:
        flash('차단된 상품입니다.', 'error')
        return redirect(url_for('product.list_products'))
    seller = User.query.get(product.seller_id)
    return render_template('view_product.html', product=product, seller=seller)



@product_bp.route('/products/new', methods=['GET', 'POST'])
def new_product():
    if 'user_id' not in session:
        flash('로그인이 필요합니다.', 'error')
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        description = request.form.get('description', '').strip()
        price = request.form.get('price', '').strip()
        file = request.files.get('image')

        # 필수값 검증
        if not title or not description or not price.isdigit():
            flash('모든 필드를 정확히 입력해주세요.', 'error')
            return redirect(url_for('product.new_product'))

        image_url = None
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            image_url = f'/static/uploads/{filename}'
        elif file:
            flash('이미지 파일 형식이 올바르지 않습니다.', 'error')
            return redirect(url_for('product.new_product'))

        product = Product(
            seller_id=session['user_id'],
            title=title,
            description=description,
            price=int(price),
            image_url=image_url
        )
        db.session.add(product)
        db.session.commit()
        flash('상품이 등록되었습니다.', 'success')
        return redirect(url_for('product.list_products'))

    return render_template('new_product.html')

