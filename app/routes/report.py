from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.models import db, Report
from app.forms.forms import ReportForm  #  새로 추가

report_bp = Blueprint('report', __name__)  #  Blueprint 먼저 생성

@report_bp.route('/report', methods=['GET', 'POST'])  #  그 다음에 데코레이터 사용
def report():
    if 'user_id' not in session:
        flash('로그인이 필요합니다.', 'error')
        return redirect(url_for('auth.login'))

    form = ReportForm()

    if form.validate_on_submit():
        new_report = Report(
            reporter_id=session['user_id'],
            target_type=form.target_type.data,
            target_id=form.target_id.data,
            reason=form.reason.data
        )
        db.session.add(new_report)
        db.session.commit()
        flash('신고가 접수되었습니다.', 'success')
        return redirect(url_for('dashboard.user_dashboard'))

    return render_template('report.html', form=form)