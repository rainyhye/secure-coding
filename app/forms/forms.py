# app/forms/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Email, Length, NumberRange
from flask_wtf.file import FileField, FileAllowed

class RegisterForm(FlaskForm):
    username = StringField('사용자 이름', validators=[DataRequired(), Length(min=3, max=20)])
    email = StringField('이메일', validators=[DataRequired(), Email()])
    password = PasswordField('비밀번호', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('회원가입')

class LoginForm(FlaskForm):
    username = StringField('사용자 이름', validators=[DataRequired()])
    password = PasswordField('비밀번호', validators=[DataRequired()])
    submit = SubmitField('로그인')

class ProductForm(FlaskForm):
    title = StringField('제목', validators=[DataRequired()])
    description = TextAreaField('설명', validators=[DataRequired()])
    price = IntegerField('가격', validators=[DataRequired(), NumberRange(min=0)])
    image = FileField('이미지', validators=[
        FileAllowed(['jpg', 'png', 'jpeg', 'gif'], '이미지 파일만 업로드할 수 있습니다.')
    ])
    submit = SubmitField('상품 등록')
    
class ProfileForm(FlaskForm):
    bio = TextAreaField('소개글', validators=[Length(max=500)])
    submit = SubmitField('프로필 업데이트')

class TransferForm(FlaskForm):
    receiver_username = StringField('받는 사람 사용자명', validators=[DataRequired()])
    amount = IntegerField('송금 금액', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('송금하기')

class RechargeForm(FlaskForm):
    amount = IntegerField('충전 금액', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('충전하기')

class ReportForm(FlaskForm):
    target_type = StringField('신고 대상 유형', validators=[DataRequired()])
    target_id = IntegerField('대상 ID', validators=[DataRequired()])
    reason = TextAreaField('신고 사유', validators=[DataRequired()])
    submit = SubmitField('신고 제출')
