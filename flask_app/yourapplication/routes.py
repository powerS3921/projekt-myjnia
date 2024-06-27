from flask import Blueprint, render_template, url_for, flash, redirect, request
from flask_login import login_user, current_user, logout_user, login_required
from yourapplication.forms import RegistrationForm, LoginForm, CarWashForm
from yourapplication.models import User, CarWash, Admin, ExternalUser, ChemicalsInventory, InterfaceValidatorFormularza, Raport, ObslugaRaportu, db

bp = Blueprint('routes', __name__, url_prefix='/routes')

@bp.route("/")
@bp.route("/home")
def home():
    return render_template('home.html')

@bp.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('routes.login'))
    return render_template('register.html', title='Register', form=form)

@bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('routes.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('create_carwash.html', title='Login', form=form)

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('routes.home'))

@bp.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')

@bp.route("/carwash/new", methods=['GET', 'POST'])
@login_required
def new_carwash():
    form = CarWashForm()
    if form.validate_on_submit():
        current_user.addCarWash(name=form.name.data, location=form.location.data)
        flash('Your carwash has been created!', 'success')
        return redirect(url_for('routes.home'))
    return render_template('create_carwash.html', title='New Carwash', form=form)
