# app/routes/report.py
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.models import db, Report

report_bp = Blueprint('report', __name__)

@report_bp.route('/report', methods=['GET', 'POST'])
def report():
    if 'user_id' not in session:
        flash('로그인이 필요합니다.', 'error')
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        target_type = request.form.get('target_type')  # 'user' or 'product'
        target_id = request.form.get('target_id')
        reason = request.form.get('reason')

        if not target_type or not target_id or not reason:
            flash('모든 필드를 입력해주세요.', 'error')
            return redirect(url_for('report.report'))

        new_report = Report(
            reporter_id=session['user_id'],
            target_type=target_type,
            target_id=int(target_id),
            reason=reason
        )
        db.session.add(new_report)
        db.session.commit()

        flash('신고가 접수되었습니다.', 'success')
        return redirect(url_for('dashboard.user_dashboard'))

    return render_template('report.html')